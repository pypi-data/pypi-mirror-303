#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import pytest
import torch
from pytorch_lightning.strategies.ddp import DDPStrategy
from torch.utils.data import Dataset, TensorDataset
from torchvision.datasets import FakeData

from lightly_train._commands import train_helpers
from lightly_train._loggers.jsonl import JSONLLogger
from lightly_train._methods.simclr import (
    SimCLR,
    SimCLRArgs,
    SimCLRTransform,
    SimCLRTransformArgs,
)
from lightly_train._models import package_helpers
from lightly_train._models.custom.custom import CustomFeatureExtractor
from lightly_train._optim.adamw_args import AdamWArgs
from lightly_train._scaling import IMAGENET_SIZE, ScalingInfo
from lightly_train._transforms.transform import NormalizeArgs
from lightly_train.errors import ConfigValidationError

from .. import helpers
from ..helpers import DummyCustomModel

REPRESENTATIVE_MODEL_NAMES = [
    "timm/vit_tiny_patch16_224",
    "timm/resnet18",
    "torchvision/convnext_tiny",
    "torchvision/resnet18",
]


def test_get_transform__method() -> None:
    assert isinstance(
        train_helpers.get_transform(
            method="simclr", transform_args_resolved=SimCLRTransformArgs()
        ),
        SimCLRTransform,
    )


def test_get_transform__method_and_transform_dict() -> None:
    transform = train_helpers.get_transform(
        method="simclr",
        transform_args_resolved=SimCLRTransformArgs(random_gray_scale=0.42),
    )
    assert isinstance(transform, SimCLRTransform)
    assert transform.transform_args.random_gray_scale == 0.42


@pytest.mark.parametrize("mmap_file", ["test.pyarrow", None])
def test_get_dataset__path(tmp_path: Path, mmap_file: str) -> None:
    (tmp_path / "img.jpg").touch()
    mmap_filepath = tmp_path / mmap_file if mmap_file is not None else None
    _ = train_helpers.get_dataset(
        data=tmp_path,
        transform=None,
        mmap_filepath=mmap_filepath,
    )


def test_get_dataset__path__nonexisting(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        train_helpers.get_dataset(
            data=tmp_path / "nonexisting",
            transform=None,
            mmap_filepath=None,
        )


def test_get_dataset__path__nondir(tmp_path: Path) -> None:
    file = tmp_path / "img.jpg"
    file.touch()
    with pytest.raises(ValueError):
        train_helpers.get_dataset(
            data=file,
            transform=None,
            mmap_filepath=None,
        )


def test_get_dataset__path__empty(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        train_helpers.get_dataset(
            data=tmp_path,
            transform=None,
            mmap_filepath=None,
        )


def test_get_dataset__dataset() -> None:
    dataset = torch.utils.data.TensorDataset(torch.rand(10, 3, 224, 224))
    dataset_1 = train_helpers.get_dataset(
        data=dataset,
        transform=None,
        mmap_filepath=None,
    )
    assert dataset == dataset_1


@pytest.mark.parametrize(
    "num_nodes, num_devices, global_batch_size, expected_batch_size",
    [
        (1, 1, 8, 8),
        (1, 2, 8, 4),
        (2, 2, 8, 2),
    ],
)
def test_get_dataloader(
    num_nodes: int, num_devices: int, global_batch_size: int, expected_batch_size: int
) -> None:
    dataset = TensorDataset(torch.rand(16, 3, 32, 32))
    dataloader = train_helpers.get_dataloader(
        dataset=dataset,
        global_batch_size=global_batch_size,
        num_nodes=num_nodes,
        num_devices=num_devices,
        num_workers=0,
        loader_args=None,
    )
    assert len(dataloader) == 16 // expected_batch_size
    batches = list(dataloader)
    assert len(batches) == 16 // expected_batch_size
    assert all(batch[0].shape == (expected_batch_size, 3, 32, 32) for batch in batches)


def test_get_dataloader__error() -> None:
    dataset = TensorDataset(torch.rand(16, 3, 32, 32))
    with pytest.raises(
        ValueError,
        match=re.escape("Batch size 8 must be divisible by (num_nodes * devices) = 3."),
    ):
        _ = train_helpers.get_dataloader(
            dataset=dataset,
            global_batch_size=8,
            num_nodes=1,
            num_devices=3,
            num_workers=0,
            loader_args=None,
        )


@pytest.mark.parametrize("model_name", REPRESENTATIVE_MODEL_NAMES)
@pytest.mark.parametrize("embed_dim", [None, 64])
@pytest.mark.parametrize("model_args", [None, {"num_classes": 42}])
def test_get_embedding_model(
    model_name: str, embed_dim: int | None, model_args: dict[str, Any] | None
) -> None:
    if model_name.startswith("timm/"):
        pytest.importorskip("timm")
    x = torch.rand(1, 3, 224, 224)
    model = package_helpers.get_model(model_name, model_args=model_args)
    embedding_model = train_helpers.get_embedding_model(model, embed_dim=embed_dim)
    embedding = embedding_model.forward(x)
    assert embedding.shape == (1, embedding_model.embed_dim, 1, 1)
    if (
        model_args is not None
        and "num_classes" in model_args
        and not model_name.startswith("torchvision/")
    ):
        assert model.num_classes == model_args["num_classes"]


@pytest.mark.parametrize("embed_dim", [None, 64])
def test_get_embedding_model__custom(embed_dim: int | None) -> None:
    model = package_helpers.get_model(model=DummyCustomModel())
    x = torch.rand(1, 3, 224, 224)
    embedding_model = train_helpers.get_embedding_model(model, embed_dim=embed_dim)
    assert isinstance(embedding_model.feature_extractor, CustomFeatureExtractor)
    embedding = embedding_model.forward(x)
    assert embedding.shape == (1, embedding_model.embed_dim, 1, 1)


def test_get_trainer(tmp_path: Path) -> None:
    trainer = train_helpers.get_trainer(
        out=tmp_path,
        epochs=1,
        accelerator="cpu",
        strategy="auto",
        devices="auto",
        num_nodes=1,
        precision=32,
        log_every_n_steps=1,
        loggers=[JSONLLogger(save_dir="logs")],
        callbacks=[],
        trainer_args=None,
    )
    assert len(trainer.loggers) == 1
    assert trainer.loggers[0].__class__.__name__ == "JSONLLogger"
    assert trainer.max_epochs == 1


def test_get_lightning_logging_interval() -> None:
    assert (
        train_helpers.get_lightning_logging_interval(dataset_size=10, batch_size=10)
        == 1
    )
    assert (
        train_helpers.get_lightning_logging_interval(dataset_size=10, batch_size=2) == 5
    )
    assert (
        train_helpers.get_lightning_logging_interval(dataset_size=1000, batch_size=10)
        == 50
    )
    assert (
        train_helpers.get_lightning_logging_interval(dataset_size=1, batch_size=10) == 1
    )


def test_get_lightning_logging_interval__fails_for_nonpositive_inputs() -> None:
    with pytest.raises(
        ValueError,
        match=r"Dataset size \(0\) and batch size \(10\) must be positive integers.",
    ):
        train_helpers.get_lightning_logging_interval(dataset_size=0, batch_size=10)
    with pytest.raises(
        ValueError,
        match=r"Dataset size \(10\) and batch size \(0\) must be positive integers.",
    ):
        train_helpers.get_lightning_logging_interval(dataset_size=10, batch_size=0)
    with pytest.raises(
        ValueError,
        match=r"Dataset size \(-10\) and batch size \(10\) must be positive integers.",
    ):
        train_helpers.get_lightning_logging_interval(dataset_size=-10, batch_size=10)
    with pytest.raises(
        ValueError,
        match=r"Dataset size \(10\) and batch size \(-10\) must be positive integers.",
    ):
        train_helpers.get_lightning_logging_interval(dataset_size=10, batch_size=-10)


_DDP_STRATEGY = DDPStrategy()


@pytest.mark.parametrize(
    "strategy, accelerator, devices, expected",
    [
        ("ddp", "auto", "auto", "ddp"),
        (_DDP_STRATEGY, "auto", "auto", _DDP_STRATEGY),
        ("auto", "cpu", "auto", "auto"),  # CPU should not use DDP by default
        ("auto", "cpu", 1, "auto"),
        ("auto", "cpu", 2, "ddp_find_unused_parameters_true"),
        ("auto", "gpu", 1, "auto"),
        ("auto", "gpu", 2, "ddp_find_unused_parameters_true"),
    ],
)
def test_get_strategy(
    strategy: str | DDPStrategy,
    accelerator: str,
    devices: str | int,
    expected: str | DDPStrategy,
) -> None:
    if accelerator == "gpu":
        if not torch.cuda.is_available():
            pytest.skip("No GPU available.")
        assert isinstance(devices, int)
        if devices > torch.cuda.device_count():
            pytest.skip("Not enough GPUs available.")

    assert (
        train_helpers.get_strategy(
            strategy=strategy, accelerator=accelerator, devices=devices
        )
        == expected
    )


@pytest.mark.parametrize(
    "optim_args, expected",
    [
        (None, AdamWArgs()),
        ({}, AdamWArgs()),
        ({"lr": 0.1, "betas": [0.2, 0.3]}, AdamWArgs(lr=0.1, betas=(0.2, 0.3))),
        (AdamWArgs(), AdamWArgs()),
    ],
)
def test_get_optimizer_args(
    optim_args: dict[str, Any] | None, expected: AdamWArgs
) -> None:
    method = helpers.get_method()
    assert (
        train_helpers.get_optimizer_args(optim_args=optim_args, method=method)
        == expected
    )


@pytest.mark.parametrize(
    "dataset, expected",
    [
        (FakeData(size=2), ScalingInfo(dataset_size=2)),
        (iter(FakeData(size=2)), ScalingInfo(dataset_size=IMAGENET_SIZE)),
    ],
)
def test_get_scaling_info(dataset: Dataset, expected: ScalingInfo) -> None:
    assert train_helpers.get_scaling_info(dataset=dataset) == expected


@pytest.mark.parametrize(
    "args,expected",
    [
        (None, SimCLRArgs()),
        ({}, SimCLRArgs()),
        (
            {
                "hidden_dim": 42,
            },
            SimCLRArgs(hidden_dim=42),
        ),
        (SimCLRArgs(hidden_dim=42), SimCLRArgs(hidden_dim=42)),
    ],
)
def test_get_method_args(
    args: dict[str, Any] | SimCLRArgs | None, expected: SimCLRArgs
) -> None:
    scaling_info = ScalingInfo(dataset_size=2)
    embedding_model = helpers.get_embedding_model()
    resolved_args = train_helpers.get_method_args(
        method="simclr",
        method_args=args,
        scaling_info=scaling_info,
        embedding_model=embedding_model,
    )
    assert resolved_args == expected


def test_get_method() -> None:
    embedding_model = helpers.get_embedding_model()
    method = train_helpers.get_method(
        method="simclr",
        method_args=SimCLRArgs(temperature=0.2),
        embedding_model=embedding_model,
        batch_size_per_device=1,
    )
    assert isinstance(method, SimCLR)
    assert method.method_args.temperature == 0.2
    assert method.batch_size_per_device == 1
    assert method.embedding_model == embedding_model


@pytest.mark.parametrize(
    "transform_dict, expected_result",
    [
        # Test case for default empty dictionary
        ({}, SimCLRTransformArgs()),
        # Test case for None input
        (None, SimCLRTransformArgs()),
        # Test case for user config
        (
            {"normalize": {"mean": (0.5, 0.5, 0.5), "std": (0.5, 0.5, 0.5)}},
            SimCLRTransformArgs(
                normalize=NormalizeArgs(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
            ),
        ),
        # Test case of SimCLRTransformArgs input
        (
            SimCLRTransformArgs(
                normalize=NormalizeArgs(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
            ),
            SimCLRTransformArgs(
                normalize=NormalizeArgs(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
            ),
        ),
    ],
)
def test_get_transform_args__success(transform_dict, expected_result) -> None:
    transform_args = train_helpers.get_transform_args(
        method="simclr", transform_args=transform_dict
    )
    assert transform_args == expected_result


def test_get_transform_args__failure() -> None:
    with pytest.raises(ConfigValidationError):
        train_helpers.get_transform_args(
            method="simclr",
            transform_args={"nonexisting_arg": 1},
        )
