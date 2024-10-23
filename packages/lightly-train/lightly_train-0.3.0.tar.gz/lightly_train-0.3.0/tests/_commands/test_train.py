#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Literal

import pytest
import torch
from omegaconf import OmegaConf
from pytest import LogCaptureFixture
from pytest_mock import MockerFixture

from lightly_train._callbacks.callback_args import CallbackArgs
from lightly_train._checkpoint import Checkpoint
from lightly_train._commands import train
from lightly_train._commands.train import (
    CLITrainConfig,
    FunctionTrainConfig,
    TrainConfig,
)
from lightly_train._loggers.logger_args import LoggerArgs
from lightly_train._methods import method_helpers
from lightly_train._methods.dino import DINOAdamWArgs, DINOArgs, DINOTransformArgs

from .. import helpers

try:
    import tensorboard
except ImportError:
    tensorboard = None


def test_train__cpu(tmp_path: Path) -> None:
    out = tmp_path / "out"
    data = tmp_path / "data"
    helpers.create_images(image_dir=data, n=10)

    train.train(
        out=out,
        data=data,
        model="torchvision/resnet18",
        method="simclr",
        batch_size=4,
        num_workers=2,
        epochs=1,
        accelerator="cpu",
    )

    # Check that the correct files were created.
    filepaths = {fp.relative_to(out) for fp in out.rglob("*")}
    expected_filepaths = {
        Path("checkpoints"),
        Path("checkpoints") / "epoch=0-step=2.ckpt",
        Path("checkpoints") / "last.ckpt",
        Path("metrics.jsonl"),
        Path("train.log"),
    }
    if tensorboard is not None:
        # Tensorboard filename is not deterministic, so we need to find it.
        tensorboard_filepath = next(
            fp for fp in filepaths if fp.name.startswith("events.out.tfevents")
        )
        expected_filepaths.add(tensorboard_filepath)

    assert filepaths == expected_filepaths


@pytest.mark.skipif(not torch.cuda.is_available(), reason="Test requires GPU.")
@pytest.mark.parametrize("num_workers", [0, 2, "auto"])
def test_train(
    tmp_path: Path, caplog: LogCaptureFixture, num_workers: int | Literal["auto"]
) -> None:
    out = tmp_path / "out"
    data = tmp_path / "data"
    helpers.create_images(image_dir=data, n=10)

    train.train(
        out=out,
        data=data,
        model="torchvision/resnet18",
        method="simclr",
        batch_size=4,
        num_workers=num_workers,
        epochs=1,
        devices=1,
    )

    # Check that we can resume training
    last_ckpt_path = out / "checkpoints" / "last.ckpt"
    with caplog.at_level(logging.INFO):
        train.train(
            out=out,
            data=data,
            model="torchvision/resnet18",
            method="simclr",
            batch_size=4,
            num_workers=2,
            epochs=2,
            devices=1,
            resume=True,
        )
    assert (
        f"Restoring states from the checkpoint path at {last_ckpt_path}" in caplog.text
    )
    # Epochs in checkpoint are 0-indexed. Epoch 1 is therefore the second epoch.
    assert torch.load(last_ckpt_path)["epoch"] == 1


@pytest.mark.skipif(not torch.cuda.is_available(), reason="Test requires GPU.")
def test_train__overwrite_true(tmp_path: Path) -> None:
    """Test that overwrite=True allows training with an existing output directory that
    contains files."""
    out = tmp_path / "out"
    data = tmp_path / "data"
    out.mkdir(parents=True, exist_ok=True)
    (out / "file.txt").touch()
    helpers.create_images(image_dir=data, n=10)

    train.train(
        out=out,
        data=data,
        model="torchvision/resnet18",
        method="simclr",
        batch_size=4,
        num_workers=2,
        epochs=1,
        devices=1,
        overwrite=True,
    )


@pytest.mark.skipif(not torch.cuda.is_available(), reason="Test requires GPU.")
def test_train__overwrite_false(tmp_path: Path) -> None:
    (tmp_path / "file.txt").touch()

    with pytest.raises(ValueError):
        train.train(
            out=tmp_path,
            data=tmp_path,
            model="torchvision/resnet18",
            method="simclr",
            batch_size=4,
            num_workers=2,
            epochs=1,
        )


@pytest.mark.skipif(not torch.cuda.is_available(), reason="Test requires GPU.")
def test_train__embed_dim(tmp_path: Path) -> None:
    out = tmp_path / "out"
    data = tmp_path / "data"
    helpers.create_images(image_dir=data, n=10)

    train.train(
        out=out,
        data=data,
        model="torchvision/resnet18",
        method="simclr",
        batch_size=4,
        num_workers=2,
        epochs=1,
        devices=1,
        embed_dim=64,
    )


@pytest.mark.skipif(not torch.cuda.is_available(), reason="Test requires GPU.")
def test_train__custom_model(tmp_path: Path) -> None:
    out = tmp_path / "out"
    data = tmp_path / "data"
    helpers.create_images(image_dir=data, n=10)

    train.train(
        out=out,
        data=data,
        model=helpers.DummyCustomModel(),
        method="simclr",
        batch_size=4,
        num_workers=2,
        devices=1,
        epochs=1,
    )


@pytest.mark.skipif(
    sys.version_info < (3, 10), reason="Requires Python 3.10 or higher for typing."
)
def test_train__parameters() -> None:
    """Tests that train function and TrainConfig have the same parameters and default
    values.

    This test is here to make sure we don't forget to update train/TrainConfig when
    we change parameters in one of the two.
    """
    helpers.assert_same_params(a=FunctionTrainConfig, b=train.train)
    helpers.assert_same_params(a=TrainConfig, b=FunctionTrainConfig, assert_type=False)
    helpers.assert_same_params(a=TrainConfig, b=CLITrainConfig, assert_type=False)


@pytest.mark.skipif(not torch.cuda.is_available(), reason="Test requires GPU.")
def test_train__zero_epochs(tmp_path: Path) -> None:
    out = tmp_path / "out"
    data = tmp_path / "data"
    helpers.create_images(image_dir=data, n=10)
    train.train(
        out=out,
        data=data,
        model="torchvision/resnet18",
        method="simclr",
        batch_size=4,
        num_workers=2,
        devices=1,
        epochs=0,
    )
    assert (out / "checkpoints" / "last.ckpt").exists()


@pytest.mark.skipif(not torch.cuda.is_available(), reason="Test requires GPU.")
def test_train_from_dictconfig(tmp_path: Path) -> None:
    out = tmp_path / "out"
    data = tmp_path / "data"
    helpers.create_images(image_dir=data, n=10)
    config = OmegaConf.create(
        dict(
            out=str(out),
            data=str(data),
            model="torchvision/resnet18",
            method="simclr",
            batch_size=4,
            num_workers=2,
            epochs=1,
            devices=1,
            optim_args={"lr": 0.1, "betas": [0.9, 0.99]},
            loader_args={"shuffle": True},
            trainer_args={"min_epochs": 1},
            model_args={"num_classes": 42},
            callbacks={"model_checkpoint": {"every_n_epochs": 5}},
            loggers={"jsonl": {"flush_logs_every_n_steps": 5}},
        )
    )
    train.train_from_dictconfig(config=config)


@pytest.mark.skipif(not torch.cuda.is_available(), reason="Test requires GPU.")
@pytest.mark.parametrize("method", method_helpers.list_methods())
@pytest.mark.parametrize(
    "devices", [1]
)  # TODO(Philipp, 09/24): Add test with 2 devices back.
def test_train__method(tmp_path: Path, method: str, devices: int) -> None:
    if torch.cuda.device_count() < devices:
        pytest.skip("Test requires more GPUs than available.")

    out = tmp_path / "out"
    data = tmp_path / "data"
    helpers.create_images(image_dir=data, n=10)

    train.train(
        out=out,
        data=data,
        model="torchvision/resnet18",
        devices=devices,
        method=method,
        batch_size=4,
        num_workers=2,
        epochs=1,
    )


@pytest.mark.skipif(not torch.cuda.is_available(), reason="Test requires GPU.")
def test_train__checkpoint_gradients(tmp_path: Path) -> None:
    """Test that checkpoints saved during training do not have disabled gradients.

    This is especially a problem for methods with momentum encoders (e.g. DINO) where
    the momentum encoder does not receive gradients during training. As the momentum
    encoder is used for finetuning, we want to make sure that it doesn't have gradients
    disabled in the checkpoint as this can result in subtle bugs where users don't
    realize that the model is frozen while finetuning.
    """
    out = tmp_path / "out"
    data = tmp_path / "data"
    helpers.create_images(image_dir=data, n=10)

    train.train(
        out=out,
        data=data,
        model="torchvision/resnet18",
        method="dino",
        batch_size=4,
        num_workers=2,
        epochs=1,
        devices=1,
    )
    ckpt_path = out / "checkpoints" / "last.ckpt"
    ckpt = Checkpoint.from_path(checkpoint=ckpt_path)
    for param in ckpt.lightly_train.models.model.parameters():
        assert param.requires_grad


def test_train__TrainConfig__model_dump(tmp_path: Path) -> None:
    """
    Test that TrainConfig is dumped correctly even if some of its attributes are
    subclasses of the types specified in the TrainConfig class.
    """
    out = tmp_path / "out"
    data = tmp_path / "data"
    config = TrainConfig(
        out=out,
        data=data,
        model="torchvision/resnet18",
        method="simclr",
        optim_args=DINOAdamWArgs(),
        method_args=DINOArgs(),
    )
    dumped_config_direct = config.model_dump()

    # Assert that the indirect dump is the same as the direct dump.
    dumped_cofig_indirect = {
        key: value.model_dump() if hasattr(value, "model_dump") else value
        for key, value in config.__dict__.items()
    }
    assert dumped_config_direct == dumped_cofig_indirect

    # Check for some specific attributes.
    assert dumped_config_direct["optim_args"]["betas"] == (0.9, 0.999)
    assert dumped_config_direct["method_args"]["warmup_teacher_temp_epochs"] == 30


def test_train__log_resolved_config__args(
    mocker: MockerFixture, tmp_path: Path
) -> None:
    """Test that log_resolved_config is called with resolved arguments."""
    out = tmp_path / "out"
    data = tmp_path / "data"
    helpers.create_images(image_dir=data, n=10)

    spy_log_resolved_config = mocker.spy(train, "log_resolved_config")

    train.train(
        out=out,
        data=data,
        model="torchvision/resnet18",
        method="dino",
        batch_size=4,
        num_workers=0,
        epochs=0,
        accelerator="cpu",
    )

    expected_config = TrainConfig(
        out=out,
        data=data,
        model="torchvision/resnet18",
        method="dino",
        batch_size=4,
        num_workers=0,
        epochs=0,
        accelerator="cpu",
        method_args=DINOArgs(output_dim=1024, teacher_temp=0.02, momentum_start=0.99),
        loggers=LoggerArgs(),
        callbacks=CallbackArgs(),
        optim_args=DINOAdamWArgs(),
        transform_args=DINOTransformArgs(),
    )

    spy_log_resolved_config.assert_called_once()
    first_call = spy_log_resolved_config.call_args_list[0]
    passed_config = first_call.kwargs["config"]
    # Assert that the dicts are equal, as the object addresses are not equal.
    assert passed_config == expected_config
