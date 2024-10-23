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
from typing import Any, Callable, Sized, Type

from pytorch_lightning import Callback, Trainer
from pytorch_lightning.accelerators.accelerator import Accelerator
from pytorch_lightning.accelerators.cpu import CPUAccelerator
from pytorch_lightning.accelerators.cuda import CUDAAccelerator
from pytorch_lightning.loggers import Logger
from pytorch_lightning.strategies.strategy import Strategy
from pytorch_lightning.trainer.connectors.accelerator_connector import _PRECISION_INPUT
from torch.nn import Module
from torch.utils.data import DataLoader, Dataset

from lightly_train._configs import validate
from lightly_train._constants import DATALOADER_TIMEOUT
from lightly_train._data import image_dataset
from lightly_train._data._serialize import memory_mapped_sequence
from lightly_train._data.image_dataset import ImageDataset
from lightly_train._methods import method_helpers
from lightly_train._methods.method import Method
from lightly_train._methods.method_args import MethodArgs
from lightly_train._models import package_helpers
from lightly_train._models.embedding_model import EmbeddingModel
from lightly_train._optim.optimizer_args import OptimizerArgs
from lightly_train._optim.optimizer_type import OptimizerType
from lightly_train._scaling import IMAGENET_SIZE, ScalingInfo
from lightly_train._transforms.transform import MethodTransform, MethodTransformArgs
from lightly_train.types import PathLike

logger = logging.getLogger(__name__)


def get_transform_args(
    method: str | Method, transform_args: dict[str, Any] | MethodTransformArgs | None
) -> MethodTransformArgs:
    logger.debug(f"Getting transform args for method '{method}'.")
    logger.debug(f"Using additional transform arguments {transform_args}.")
    if isinstance(transform_args, MethodTransformArgs):
        return transform_args

    method_cls = method_helpers.get_method_cls(method)
    transform_cls = method_cls.transform_cls()
    transform_args_cls = transform_cls.transform_args_cls()

    if transform_args is None:
        return transform_args_cls()

    return validate.pydantic_model_validate(transform_args_cls, transform_args)


def get_transform(
    method: str | Method,
    transform_args_resolved: MethodTransformArgs,
) -> MethodTransform:
    logger.debug(f"Getting transform for method '{method}'.")
    validate.assert_config_resolved(transform_args_resolved)
    method_cls = method_helpers.get_method_cls(method)
    transform_cls = method_cls.transform_cls()
    transform = transform_cls(transform_args=transform_args_resolved)
    return transform


def get_dataset(
    data: PathLike | Dataset,
    transform: Callable | None,
    mmap_filepath: Path | None,
) -> Dataset:
    if isinstance(data, Dataset):
        logger.debug("Using provided dataset.")
        return data

    data = Path(data).resolve()
    logger.debug(f"Making sure data directory '{data}' exists and is not empty.")
    if not data.exists():
        raise ValueError(f"Data directory '{data}' does not exist!")
    elif not data.is_dir():
        raise ValueError(f"Data path '{data}' is not a directory!")
    elif data.is_dir() and not any(data.iterdir()):
        raise ValueError(f"Data directory '{data}' is empty!")

    logger.debug(f"Loading ImageDataset from '{data}'.")
    filenames = image_dataset.list_image_filenames(image_dir=data)
    if mmap_filepath is not None:
        return ImageDataset(
            image_dir=data,
            image_filenames=memory_mapped_sequence.memory_mapped_sequence_from_filenames(
                filenames=filenames,
                mmap_filepath=mmap_filepath,
            ),
            transform=transform,
        )
    else:
        return ImageDataset(
            image_dir=data,
            image_filenames=list(filenames),
            transform=transform,
        )


def get_dataloader(
    dataset: Dataset,
    global_batch_size: int,
    num_nodes: int,
    num_devices: int,
    num_workers: int,
    loader_args: dict[str, Any] | None,
) -> DataLoader:
    """Creates a dataloader for the given dataset.

    Args:
        dataset:
            Dataset.
        global_batch_size:
            The global batch size. This is the total batch size across all nodes and
            devices. The batch size for the dataloader is calculated as
            global_batch_size // (num_nodes * num_devices).
        num_nodes:
            Number of nodes.
        num_devices:
            Number of devices per node.
        num_workers:
            Number of workers for the dataloader.
        loader_args:
            Additional arguments for the DataLoader. Additional arguments have priority
            over other arguments.

    Raises:
        ValueError: If the global batch size is not divisible by
        (num_nodes * num_devices).
    """
    logger.debug(f"Getting dataloader with num_workers {num_workers}.")
    # We call it devices instead of num_devices in user-facing messages because thats
    # how the argument is called in the config.
    logger.debug(f"Using num_nodes {num_nodes} and devices {num_devices}.")
    # Limit batch size for small datasets.
    if isinstance(dataset, Sized):
        dataset_size = len(dataset)
        logger.debug(f"Detected dataset size {dataset_size}.")
        if dataset_size < global_batch_size:
            old_global_batch_size = global_batch_size
            global_batch_size = dataset_size
            logger.warning(
                f"Detected dataset size {dataset_size} and batch size "
                f"{old_global_batch_size}. Reducing batch size to {global_batch_size}."
            )
    logger.debug(
        f"Getting batch size per device from global batch size {global_batch_size}."
    )
    # NOTE(Guarin, 09/24): We don't use the trainer.world_size attribute to calculate
    # the total number of devices because it doesn't always work correctly with SLURM.
    total_devices = num_nodes * num_devices
    if global_batch_size % total_devices != 0:
        raise ValueError(
            f"Batch size {global_batch_size} must be divisible by "
            f"(num_nodes * devices) = {total_devices}."
        )
    batch_size = global_batch_size // total_devices
    logger.debug(f"Using batch size per device {batch_size}.")
    timeout = DATALOADER_TIMEOUT if num_workers > 0 else 0
    dataloader_kwargs: dict[str, Any] = dict(
        dataset=dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        drop_last=True,
        timeout=timeout,
    )
    if loader_args is not None:
        logger.debug(f"Using additional dataloader arguments {loader_args}.")
        dataloader_kwargs.update(**loader_args)
    return DataLoader(**dataloader_kwargs)


def get_embedding_model(model: Module, embed_dim: int | None = None) -> EmbeddingModel:
    logger.debug(f"Getting embedding model with embedding dimension {embed_dim}.")
    feature_extractor_cls = package_helpers.get_feature_extractor_cls(model=model)
    feature_extractor = feature_extractor_cls(model=model)
    return EmbeddingModel(feature_extractor=feature_extractor, embed_dim=embed_dim)


def get_trainer(
    out: Path,
    epochs: int,
    accelerator: str | Accelerator,
    strategy: str | Strategy,
    devices: list[int] | str | int,
    num_nodes: int,
    log_every_n_steps: int,
    precision: _PRECISION_INPUT | None,
    loggers: list[Logger],
    callbacks: list[Callback],
    trainer_args: dict[str, Any] | None,
) -> Trainer:
    logger.debug("Getting trainer.")

    sync_batchnorm = get_sync_batchnorm(accelerator=accelerator)

    trainer_kwargs: dict[str, Any] = dict(
        default_root_dir=out,
        max_epochs=epochs,
        accelerator=accelerator,
        strategy=strategy,
        devices=devices,
        num_nodes=num_nodes,
        precision=precision,
        log_every_n_steps=log_every_n_steps,
        callbacks=callbacks,
        logger=loggers,
        sync_batchnorm=sync_batchnorm,
    )
    if trainer_args is not None:
        logger.debug(f"Using additional trainer arguments {trainer_args}.")
        trainer_kwargs.update(trainer_args)

    return Trainer(**trainer_kwargs)


def get_lightning_logging_interval(dataset_size: int, batch_size: int) -> int:
    """Calculates the logging interval for the given dataset and batch size.

    If the number of batches is smaller than the logging interval, Lightning
    raises a UserWarning. To avoid this, we take the minimum of 50 and the number
    of batches.
    """
    if dataset_size <= 0 or batch_size <= 0:
        raise ValueError(
            f"Dataset size ({dataset_size}) and batch size ({batch_size}) must be positive integers."
        )
    n_batches = max(1, dataset_size // batch_size)
    return min(50, n_batches)  # Lightning uses 50 as default logging interval.


def get_strategy(
    strategy: str | Strategy,
    accelerator: str | Accelerator,
    devices: list[int] | str | int,
) -> str | Strategy:
    if strategy != "auto":
        logger.debug(f"Using provided strategy '{strategy}'.")
        return strategy

    accelerator_cls: Type[CUDAAccelerator] | Type[CPUAccelerator]
    if isinstance(accelerator, CUDAAccelerator) or accelerator == "gpu":
        accelerator_cls = CUDAAccelerator
    elif isinstance(accelerator, CPUAccelerator) or accelerator == "cpu":
        accelerator_cls = CPUAccelerator
    else:
        # For non CPU/CUDA accelerators we let PyTorch Lightning decide.
        logger.debug(
            "Non CPU/CUDA accelerator, using default strategy by PyTorchLightning."
        )
        return strategy

    if devices == "auto":
        num_devices = accelerator_cls.auto_device_count()
    else:
        parsed_devices = accelerator_cls.parse_devices(devices=devices)
        # None means that no devices were requested.
        if parsed_devices is None:
            return strategy
        num_devices = (
            len(parsed_devices) if isinstance(parsed_devices, list) else parsed_devices
        )
    logger.debug(f"Detected {num_devices} devices.")

    if num_devices > 1:
        # If we have multiple CPU or CUDA devices, use DDP with find_unused_parameters.
        # find_unused_parameters avoids DDP errors for models/methods that have
        # extra parameters which are not used in all the forward passes. This is for
        # example the case in DINO where the projection head is frozen during the first
        # epoch.
        # TODO: Only set find_unused_parameters=True if necessary as it slows down
        # training speed. See https://github.com/pytorch/pytorch/pull/44826 on how
        # parameters can be ignored for DDP.
        logger.debug("Using strategy 'ddp_find_unused_parameters_true'.")
        return "ddp_find_unused_parameters_true"

    logger.debug(f"Using strategy '{strategy}'.")
    return strategy


def get_sync_batchnorm(accelerator: str | Accelerator) -> bool:
    # SyncBatchNorm is only supported on CUDA devices.
    assert accelerator != "auto"
    use_sync_batchnorm = accelerator == "gpu" or isinstance(
        accelerator, CUDAAccelerator
    )
    logger.debug(f"Using sync_batchnorm '{use_sync_batchnorm}'.")
    return use_sync_batchnorm


def get_optimizer_args(
    optim_args: dict[str, Any] | OptimizerArgs | None,
    method: Method,
) -> OptimizerArgs:
    if isinstance(optim_args, OptimizerArgs):
        return optim_args
    # Hardcode OptimizerType.ADAMW for now as it is the only supported optimizer.
    optim_type = OptimizerType.ADAMW
    logger.debug(f"Using optimizer '{optim_type}'.")
    optim_args = {} if optim_args is None else optim_args
    optim_args_cls = method.optimizer_args_cls(optim_type=optim_type)
    return validate.pydantic_model_validate(optim_args_cls, optim_args)


def get_scaling_info(
    dataset: Dataset,
) -> ScalingInfo:
    if isinstance(dataset, Sized):
        dataset_size = len(dataset)
    else:
        logger.debug("Dataset does not have a length. Using default dataset size")
        dataset_size = IMAGENET_SIZE
    logger.debug(f"Found dataset size {dataset_size}.")
    return ScalingInfo(dataset_size=dataset_size)


def get_method_args(
    method: str,
    method_args: dict[str, Any] | MethodArgs | None,
    scaling_info: ScalingInfo,
    embedding_model: EmbeddingModel,
) -> MethodArgs:
    logger.debug(f"Getting method args for '{method}'")
    if isinstance(method_args, MethodArgs):
        return method_args
    method_cls = method_helpers.get_method_cls(method=method)
    method_args = {} if method_args is None else method_args
    method_args_cls = method_cls.method_args_cls()
    args = validate.pydantic_model_validate(method_args_cls, method_args)
    args.resolve_auto(scaling_info=scaling_info)
    return args


def get_method(
    method: str,
    method_args: MethodArgs,
    embedding_model: EmbeddingModel,
    batch_size_per_device: int,
) -> Method:
    logger.debug(f"Getting method for '{method}'")
    method_cls = method_helpers.get_method_cls(method=method)
    return method_cls(
        method_args=method_args,
        embedding_model=embedding_model,
        batch_size_per_device=batch_size_per_device,
    )
