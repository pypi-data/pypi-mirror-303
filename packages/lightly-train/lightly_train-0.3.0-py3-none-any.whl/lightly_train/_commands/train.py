#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from __future__ import annotations

import logging
from pathlib import Path
from tempfile import NamedTemporaryFile

# Import old types for compatibility with omegaconf.
from typing import Any, Literal

import pytorch_lightning
from omegaconf import DictConfig
from pydantic import ConfigDict
from pytorch_lightning.accelerators.accelerator import Accelerator
from pytorch_lightning.strategies.strategy import Strategy
from pytorch_lightning.trainer.connectors.accelerator_connector import _PRECISION_INPUT
from torch.nn import Module
from torch.utils.data import Dataset

from lightly_train import _logging
from lightly_train._callbacks import callback_helpers
from lightly_train._callbacks.callback_args import CallbackArgs
from lightly_train._commands import _warnings, common_helpers, train_helpers
from lightly_train._configs import omegaconf_utils, validate
from lightly_train._configs.config import PydanticConfig
from lightly_train._loggers import logger_helpers
from lightly_train._loggers.logger_args import LoggerArgs
from lightly_train._methods.method_args import MethodArgs
from lightly_train._models import package_helpers
from lightly_train._optim.optimizer_args import OptimizerArgs
from lightly_train._transforms.transform import MethodTransformArgs
from lightly_train.types import PathLike

logger = logging.getLogger(__name__)


def train(
    out: PathLike,
    data: PathLike | Dataset,
    model: str | Module,
    method: str = "simclr",
    method_args: dict[str, Any] | None = None,
    embed_dim: int | None = None,
    epochs: int = 100,
    batch_size: int = 128,
    num_workers: int | Literal["auto"] = "auto",
    devices: int | str | list[int] = "auto",
    num_nodes: int = 1,
    resume: bool = False,
    overwrite: bool = False,
    accelerator: str | Accelerator = "auto",
    strategy: str | Strategy = "auto",
    precision: _PRECISION_INPUT = "32-true",  # Default precision in PyTorch Lightning
    seed: int = 0,
    loggers: dict[str, dict[str, Any] | None] | None = None,
    callbacks: dict[str, dict[str, Any] | None] | None = None,
    optim_args: dict[str, Any] | None = None,
    transform_args: dict[str, Any] | None = None,
    loader_args: dict[str, Any] | None = None,
    trainer_args: dict[str, Any] | None = None,
    model_args: dict[str, Any] | None = None,
) -> None:
    """Train a self-supervised model.

    The training process can be monitored with TensorBoard (requires
    `pip install lightly-train[tensorboard]`):
    ```
    tensorboard --logdir out
    ```

    Args:
        out:
            Output directory to save logs, checkpoints, and other artifacts.
        data:
            Path to a directory containing images or a PyTorch Dataset.
        model:
            Model name or instance to use for training.
        method:
            Self-supervised learning method name.
        method_args:
            Arguments for the self-supervised learning method. The available arguments
            depend on the `method` parameter.
        embed_dim:
            Embedding dimension. Set this if you want to train an embedding model with
            a specific dimension. If None, the output dimension of `model` is used.
        epochs:
            Number of training epochs.
        batch_size:
            Global batch size. The batch size per device/GPU is inferred from this value
            and the number of devices and nodes.
        num_workers:
            Number of workers for the dataloader per device/GPU. 'auto' automatically
            sets the number of workers based on the available CPU cores.
        devices:
            Number of devices/GPUs to use for training. 'auto' will automatically select
            the best number of devices available.
        num_nodes:
            Number of nodes for distributed training.
        resume:
            Resume training from the last checkpoint.
        overwrite:
            Overwrite the output directory if it already exists. Warning, this might
            overwrite existing files in the directory!
        accelerator:
            Hardware accelerator. Can be one of ['cpu', 'gpu', 'tpu', 'ipu', 'hpu',
            'mps', 'auto']. 'auto' will automatically select the best accelerator
            available. For details, see:
            https://lightning.ai/docs/pytorch/stable/common/trainer.html#accelerator
        strategy:
            Training strategy. For example 'ddp' or 'auto'. 'auto' automatically
            selects the best strategy available. For details, see:
            https://lightning.ai/docs/pytorch/stable/common/trainer.html#strategy
        precision:
            Training precision. Select '16-mixed' for mixed 16-bit precision, '32-true'
            for full 32-bit precision, or 'bf16-mixed' for mixed bfloat16 precision.
            For details, see:
            https://lightning.ai/docs/pytorch/stable/common/trainer.html#precision
        seed:
            Random seed for reproducibility.
        loggers:
            Loggers for training. Either None or a dictionary of logger names to either
            None or a dictionary of logger arguments. None uses the default loggers.
            To disable a logger, set it to None: `loggers={"tensorboard": None}`.
            To configure a logger, pass the respective arguments:
            `loggers={"wandb": {"project": "my_project"}}`.
        callbacks:
            Callbacks for training. Either None or a dictionary of callback names to
            either None or a dictionary of callback arguments. None uses the default
            callbacks. To disable a callback, set it to None:
            `callbacks={"model_checkpoint": None}`. To configure a callback, pass the
            respective arguments:
            `callbacks={"model_checkpoint": {"every_n_epochs": 5}}`.
        optim_args:
            Arguments for AdamW optimizer. Available arguments are:
            - lr: float
            - betas: tuple[float, float]
            - weight_decay: float
        transform_args:
            Arguments for the image transform. The available arguments depend on the
            `method` parameter. For example, if `method='simclr'`, the arguments
            are passed to `lightly.transforms.SimCLRTransform`. See the lightly
            transforms documentation for available arguments:
            https://docs.lightly.ai/self-supervised-learning/lightly.transforms.html
        loader_args:
            Arguments for the PyTorch DataLoader. Should only be used in special cases
            as default values are automatically set. Prefer to use the `batch_size` and
            `num_workers` arguments instead. For details, see:
            https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader
        trainer_args:
            Arguments for the PyTorch Lightning Trainer. Should only be used in special
            cases as default values are automatically set. For details, see:
            https://lightning.ai/docs/pytorch/stable/common/trainer.html
        model_args:
            Arguments for the model. The available arguments depend on the `model`
            parameter. For example, if `model=f'torchvision/{model_name}'`, the arguments
            are passed to `torchvision.models.get_model(model_name, **model_args)`.
    """
    config = validate.pydantic_model_validate(TrainConfig, locals())
    train_from_config(config=config)


def train_from_config(config: TrainConfig) -> None:
    # Convert the config to a TrainConfig instance.
    config = validate.pydantic_model_validate(TrainConfig, dict(config))

    # Set up output directory.
    out_dir = common_helpers.get_out_dir(
        out=config.out, resume=config.resume, overwrite=config.overwrite
    )

    # Set up logging.
    _warnings.filter_train_warnings()
    _logging.set_up_console_logging()
    _logging.set_up_file_logging(out_dir / "train.log")
    logger.info(f"Args: {common_helpers.pretty_format_args(args=locals())}")
    logger.info(f"Using output directory '{out_dir}'.")

    pytorch_lightning.seed_everything(seed=config.seed, workers=True)
    config.transform_args = train_helpers.get_transform_args(
        method=config.method, transform_args=config.transform_args
    )
    transform_instance = train_helpers.get_transform(
        method=config.method, transform_args_resolved=config.transform_args
    )
    # Create a temporary file to use as a memory map for dataset items. The
    # file has to exist while the dataset is used.
    # TODO(Philipp, 10/24): For training it could make sense to store the
    # file in the output directory and recover it on resume.
    with NamedTemporaryFile(delete=True) as mmap_file:
        dataset = train_helpers.get_dataset(
            data=config.data,
            transform=transform_instance,
            mmap_filepath=Path(mmap_file.name),
        )
        scaling_info = train_helpers.get_scaling_info(dataset=dataset)
        model_instance = package_helpers.get_model(
            model=config.model, model_args=config.model_args
        )
        embedding_model = train_helpers.get_embedding_model(
            model=model_instance, embed_dim=config.embed_dim
        )
        log_every_n_steps = train_helpers.get_lightning_logging_interval(
            dataset_size=scaling_info.dataset_size, batch_size=config.batch_size
        )
        config.loggers = logger_helpers.get_logger_args(loggers=config.loggers)
        logger_instances = logger_helpers.get_loggers(
            logger_args=config.loggers, out=out_dir
        )
        config.callbacks = callback_helpers.get_callback_args(
            callback_args=config.callbacks
        )
        callback_instances = callback_helpers.get_callbacks(
            callback_args=config.callbacks,
            out=out_dir,
            model=model_instance,
            embedding_model=embedding_model,
            normalize_args=transform_instance.transform_args.normalize,
        )
        config.accelerator = common_helpers.get_accelerator(
            accelerator=config.accelerator
        )
        config.strategy = train_helpers.get_strategy(
            accelerator=config.accelerator,
            strategy=config.strategy,
            devices=config.devices,
        )
        trainer_instance = train_helpers.get_trainer(
            out=out_dir,
            epochs=config.epochs,
            accelerator=config.accelerator,
            strategy=config.strategy,
            devices=config.devices,
            num_nodes=config.num_nodes,
            precision=config.precision,
            log_every_n_steps=log_every_n_steps,
            loggers=logger_instances,
            callbacks=callback_instances,
            trainer_args=config.trainer_args,
        )
        num_workers = common_helpers.get_num_workers(
            num_workers=config.num_workers, num_devices=trainer_instance.num_devices
        )
        dataloader = train_helpers.get_dataloader(
            dataset=dataset,
            global_batch_size=config.batch_size,
            num_nodes=trainer_instance.num_nodes,
            num_devices=trainer_instance.num_devices,
            num_workers=num_workers,
            loader_args=config.loader_args,
        )
        assert dataloader.batch_size is not None
        config.method_args = train_helpers.get_method_args(
            method=config.method,
            method_args=config.method_args,
            scaling_info=scaling_info,
            embedding_model=embedding_model,
        )
        method_instance = train_helpers.get_method(
            method=config.method,
            method_args=config.method_args,
            embedding_model=embedding_model,
            batch_size_per_device=dataloader.batch_size,
        )
        config.optim_args = train_helpers.get_optimizer_args(
            optim_args=config.optim_args, method=method_instance
        )
        method_instance.optimizer_args = config.optim_args
        log_resolved_config(config=config)
        trainer_instance.fit(
            model=method_instance,
            train_dataloaders=dataloader,
            ckpt_path="last" if config.resume else None,
        )
    if config.epochs == 0:
        logger.info("No training epochs specified. Saving model and exiting.")
        trainer_instance.save_checkpoint(out_dir / "checkpoints" / "last.ckpt")
    logger.info("Training completed.")


def train_from_dictconfig(config: DictConfig) -> None:
    logger.debug(f"Training model with config: {config}")
    config_dict = omegaconf_utils.config_to_dict(config=config)
    train_cfg = validate.pydantic_model_validate(CLITrainConfig, config_dict)
    train_from_config(config=train_cfg)


class TrainConfig(PydanticConfig):
    out: PathLike
    data: PathLike | Dataset
    model: str | Module
    method: str = "simclr"
    method_args: dict[str, Any] | MethodArgs | None = None
    embed_dim: int | None = None
    epochs: int = 100
    batch_size: int = 128
    num_workers: int | Literal["auto"] = "auto"
    devices: int | str | list[int] = "auto"
    num_nodes: int = 1
    resume: bool = False
    overwrite: bool = False
    accelerator: str | Accelerator = "auto"
    strategy: str | Strategy = "auto"
    precision: _PRECISION_INPUT = "32-true"
    seed: int = 0
    loggers: dict[str, dict[str, Any] | None] | LoggerArgs | None = None
    callbacks: dict[str, dict[str, Any] | None] | CallbackArgs | None = None
    optim_args: dict[str, Any] | OptimizerArgs | None = None
    transform_args: dict[str, Any] | MethodTransformArgs | None = None
    loader_args: dict[str, Any] | None = None
    trainer_args: dict[str, Any] | None = None
    model_args: dict[str, Any] | None = None

    # Allow arbitrary field types such as Module, Dataset, Accelerator, ...
    model_config = ConfigDict(arbitrary_types_allowed=True)


class FunctionTrainConfig(TrainConfig):
    # Configuration with simpler types for calling the train function.
    method_args: dict[str, Any] | None = None
    loggers: dict[str, dict[str, Any] | None] | None = None
    callbacks: dict[str, dict[str, Any] | None] | None = None
    optim_args: dict[str, Any] | None = None
    transform_args: dict[str, Any] | None = None


class CLITrainConfig(FunctionTrainConfig):
    # CLI configuration with simpler types for better error messages.
    out: str
    data: str
    model: str
    accelerator: str = "auto"
    strategy: str = "auto"

    # CLI should not pass arbitrary types.
    model_config = ConfigDict(arbitrary_types_allowed=False)


def log_resolved_config(config: TrainConfig):
    """Log the resolved configuration.

    Note that the resolved configuration might still have a few values set to "auto":
    - config.strategy
    - config.devices
    """
    logger.info(
        "Resolved config:\n"
        f"{common_helpers.pretty_format_args(args=config.model_dump())}"
    )
