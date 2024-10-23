#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
"""DenseCL

- [0]: 2021, DenseCL: https://arxiv.org/abs/2011.09157
"""

from __future__ import annotations

import copy
from typing import Literal

import torch
from lightly.loss import NTXentLoss
from lightly.models import utils
from lightly.models.modules.heads import DenseCLProjectionHead
from lightly.transforms import DenseCLTransform as LightlyDenseCLTransform
from lightly.utils.scheduler import cosine_schedule
from pydantic import Field
from torch import Tensor
from torch.nn import AdaptiveAvgPool2d, Module

from lightly_train import _scaling
from lightly_train._configs.validate import no_auto
from lightly_train._methods.method import Method, TrainingStepResult
from lightly_train._methods.method_args import MethodArgs
from lightly_train._models.embedding_model import EmbeddingModel
from lightly_train._optim.trainable_modules import TrainableModules
from lightly_train._scaling import ScalingInfo
from lightly_train._transforms.transform import (
    MethodTransform,
    MethodTransformArgs,
    RandomResizeArgs,
)
from lightly_train.types import MultiViewBatch


class DenseCLArgs(MethodArgs):
    # Default values for ImageNet1k pre-training from paper.

    # Projection head
    hidden_dim: int = 2048
    output_dim: int = 128

    # Loss
    lambda_: float = 0.5
    temperature: float = 0.2
    memory_bank_size: int | Literal["auto"] = "auto"
    gather_distributed: bool = True

    # Momentum
    momentum_start: float = 0.999
    momentum_end: float = 0.999

    def resolve_auto(self, scaling_info: ScalingInfo) -> None:
        if self.memory_bank_size == "auto":
            # Reduce memory bank size for smaller datasets, otherwise training is
            # unstable.
            self.memory_bank_size = _scaling.get_bucket_value(
                input=scaling_info.dataset_size,
                buckets=[
                    (0, 0),
                    (10_000, 1024),
                    (20_000, 2048),
                    (50_000, 4096),
                    (100_000, 8192),
                    (500_000, 32768),
                    (float("inf"), 65536),
                ],
            )


class DenseCLTransformArgs(MethodTransformArgs):
    random_resize: RandomResizeArgs = Field(
        default_factory=lambda: RandomResizeArgs(min_scale=0.2)
    )


class DenseCLTransform(MethodTransform):
    def __init__(self, transform_args: DenseCLTransformArgs):
        self.transform_args = transform_args
        # Typing: LightlyDenseCLTransform is a Callable[[PILImage], list[Tensor]]
        self.transform = LightlyDenseCLTransform(
            # Typing of LightlySSL is not correct
            input_size=transform_args.image_size,  # type: ignore[arg-type]
            min_scale=transform_args.random_resize.min_scale,
            vf_prob=transform_args.random_flip.vertical_prob,
            hf_prob=transform_args.random_flip.horizontal_prob,
            normalize=(
                None
                if transform_args.normalize is None
                else transform_args.normalize.to_dict()
            ),
        )  # type: ignore[assignment]

    @staticmethod
    def transform_args_cls() -> type[DenseCLTransformArgs]:
        return DenseCLTransformArgs


class DenseCLEncoder(Module):
    def __init__(
        self,
        embedding_model: EmbeddingModel,
        hidden_dim: int,
        output_dim: int,
    ) -> None:
        super().__init__()
        self.embedding_model = embedding_model
        self.local_projection_head = DenseCLProjectionHead(
            input_dim=embedding_model.embed_dim,
            hidden_dim=hidden_dim,
            output_dim=output_dim,
        )
        self.global_projection_head = DenseCLProjectionHead(
            input_dim=embedding_model.embed_dim,
            hidden_dim=hidden_dim,
            output_dim=output_dim,
        )
        self.pool = AdaptiveAvgPool2d((1, 1))

    def forward(self, x: Tensor) -> tuple[Tensor, Tensor, Tensor]:
        # B = batch size, C = number of channels, H = image height, W = image width, D = output_dim
        # (B, C, H, W)
        features = self.embedding_model(x)
        # (B, C, H, W) -> (B, C, 1, 1) -> (B, C)
        global_proj = self.pool(features).flatten(start_dim=1)
        # (B, C) -> (B, D)
        global_proj = self.global_projection_head(global_proj)
        # (B, C, H, W) -> (B, C, H*W) -> (B, H*W, C)
        features = features.flatten(start_dim=2).permute(0, 2, 1)
        # (B, H*W, C) -> (B, H*W, D)
        local_proj = self.local_projection_head(features)
        # Return: (B, H*W, C), (B, D), (B, H*W, D)
        return features, global_proj, local_proj


class DenseCL(Method):
    """DenseCL based on MoCo v2."""

    def __init__(
        self,
        method_args: DenseCLArgs,
        embedding_model: EmbeddingModel,
        batch_size_per_device: int,
    ):
        super().__init__(
            method_args=method_args,
            embedding_model=embedding_model,
            batch_size_per_device=batch_size_per_device,
        )
        self.method_args = method_args
        self.query_encoder = DenseCLEncoder(
            embedding_model=embedding_model,
            hidden_dim=method_args.hidden_dim,
            output_dim=method_args.output_dim,
        )
        self.key_encoder = copy.deepcopy(self.query_encoder)

        self.local_criterion = NTXentLoss(
            temperature=method_args.temperature,
            memory_bank_size=(
                no_auto(method_args.memory_bank_size),
                method_args.output_dim,
            ),
            gather_distributed=method_args.gather_distributed,
        )
        self.global_criterion = copy.deepcopy(self.local_criterion)

    def training_step_impl(
        self, batch: MultiViewBatch, batch_idx: int
    ) -> TrainingStepResult:
        momentum = cosine_schedule(
            step=self.trainer.global_step,
            max_steps=self.trainer.estimated_stepping_batches,
            start_value=self.method_args.momentum_start,
            end_value=self.method_args.momentum_end,
        )
        utils.update_momentum(
            model=self.query_encoder, model_ema=self.key_encoder, m=momentum
        )
        views = batch[0]
        query_features, query_global, query_local = self.query_encoder(views[0])
        with torch.no_grad():
            key_features, key_global, key_local = self.key_encoder(views[1])

        key_local = utils.select_most_similar(query_features, key_features, key_local)
        query_local = query_local.flatten(end_dim=1)
        key_local = key_local.flatten(end_dim=1)

        local_loss = self.local_criterion(query_local, key_local)
        global_loss = self.global_criterion(query_global, key_global)
        lambda_ = self.method_args.lambda_
        loss = (1 - lambda_) * global_loss + lambda_ * local_loss

        return TrainingStepResult(loss=loss)

    @staticmethod
    def method_args_cls() -> type[DenseCLArgs]:
        return DenseCLArgs

    def trainable_modules(self) -> TrainableModules:
        return TrainableModules(modules=[self.query_encoder])

    @staticmethod
    def transform_cls() -> type[MethodTransform]:
        return DenseCLTransform
