#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from __future__ import annotations

import torch
import torch.distributed as dist
from lightly.loss import NTXentLoss
from lightly.models.modules.heads import SimCLRProjectionHead
from lightly.transforms import SimCLRTransform as LightlySimCLRTransform
from torch.nn import Flatten

from lightly_train._methods.method import Method, TrainingStepResult
from lightly_train._methods.method_args import MethodArgs
from lightly_train._models.embedding_model import EmbeddingModel
from lightly_train._optim.trainable_modules import TrainableModules
from lightly_train._transforms.transform import MethodTransform, MethodTransformArgs
from lightly_train.types import MultiViewBatch


class SimCLRArgs(MethodArgs):
    """Args for SimCLR method."""

    hidden_dim: int = 2048
    output_dim: int = 128
    num_layers: int = 2
    batch_norm: bool = True
    temperature: float = 0.1


class SimCLRTransformArgs(MethodTransformArgs):
    pass


class SimCLRTransform(MethodTransform):
    def __init__(self, transform_args: SimCLRTransformArgs):
        self.transform_args = transform_args
        # Typing: LightlySimCLRTransform is a Callable[[PILImage], list[Tensor]]
        self.transform = LightlySimCLRTransform(
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
    def transform_args_cls() -> type[SimCLRTransformArgs]:
        return SimCLRTransformArgs


class SimCLR(Method):
    def __init__(
        self,
        method_args: SimCLRArgs,
        embedding_model: EmbeddingModel,
        batch_size_per_device: int,
    ):
        super().__init__(
            method_args=method_args,
            embedding_model=embedding_model,
            batch_size_per_device=batch_size_per_device,
        )
        self.method_args = method_args
        self.embedding_model = embedding_model
        self.flatten = Flatten(start_dim=1)
        self.projection_head = SimCLRProjectionHead(
            input_dim=self.embedding_model.embed_dim,
            hidden_dim=self.method_args.hidden_dim,
            output_dim=self.method_args.output_dim,
            num_layers=self.method_args.num_layers,
            batch_norm=self.method_args.batch_norm,
        )
        self.criterion = NTXentLoss(
            temperature=self.method_args.temperature,
            gather_distributed=dist.is_available(),
        )

    def training_step_impl(
        self, batch: MultiViewBatch, batch_idx: int
    ) -> TrainingStepResult:
        views, _ = batch[0], batch[1]
        x = self.embedding_model(torch.cat(views))
        x = self.flatten(x)
        x = self.projection_head(x)
        x0, x1 = x.chunk(len(views))
        loss = self.criterion(x0, x1)

        return TrainingStepResult(loss=loss)

    @staticmethod
    def method_args_cls() -> type[SimCLRArgs]:
        return SimCLRArgs

    def trainable_modules(self) -> TrainableModules:
        return TrainableModules(modules=[self.embedding_model, self.projection_head])

    @staticmethod
    def transform_cls() -> type[MethodTransform]:
        return SimCLRTransform
