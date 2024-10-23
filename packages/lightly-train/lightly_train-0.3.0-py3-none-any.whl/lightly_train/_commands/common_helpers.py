#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from __future__ import annotations

import logging
import os
import pprint
from pathlib import Path
from typing import Any, Literal

from pytorch_lightning.accelerators.accelerator import Accelerator
from pytorch_lightning.accelerators.cpu import CPUAccelerator
from pytorch_lightning.accelerators.cuda import CUDAAccelerator
from pytorch_lightning.accelerators.mps import MPSAccelerator
from pytorch_lightning.strategies.strategy import Strategy
from torch.nn import Module

from lightly_train.types import PathLike

logger = logging.getLogger(__name__)


def get_checkpoint_path(checkpoint: PathLike) -> Path:
    checkpoint_path = Path(checkpoint).resolve()
    logger.debug(f"Making sure checkpoint '{checkpoint_path}' exists.")
    if not checkpoint_path.exists():
        raise FileNotFoundError(f"Checkpoint '{checkpoint_path}' does not exist!")
    if not checkpoint_path.is_file():
        raise ValueError(f"Checkpoint '{checkpoint_path}' is not a file!")
    return checkpoint_path


def get_out_path(out: PathLike, overwrite: bool) -> Path:
    out_path = Path(out).resolve()
    logger.debug(f"Checking if output path '{out_path}' exists.")
    if out_path.exists():
        if not overwrite:
            raise ValueError(
                f"Output '{out_path}' already exists! Set overwrite=True to overwrite "
                "the file."
            )
        if not out_path.is_file():
            raise ValueError(f"Output '{out_path}' is not a file!")
    return out_path


def get_accelerator(
    accelerator: str | Accelerator,
) -> str | Accelerator:
    logger.debug(f"Getting accelerator for '{accelerator}'.")
    if accelerator != "auto":
        # User specified an accelerator, return it.
        return accelerator

    # Default to CUDA if available.
    if CUDAAccelerator.is_available():
        logger.debug("CUDA is available, defaulting to CUDA.")
        return CUDAAccelerator()
    elif MPSAccelerator.is_available():
        logger.debug("MPS is available, defaulting to MPS.")
        return MPSAccelerator()
    else:
        logger.debug("CUDA and MPS are not available, defaulting to CPU.")
        return CPUAccelerator()


def get_out_dir(out: PathLike, resume: bool, overwrite: bool) -> Path:
    out_dir = Path(out).resolve()
    logger.debug(f"Checking if output directory '{out_dir}' exists.")
    if out_dir.exists():
        if not out_dir.is_dir():
            raise ValueError(f"Output '{out_dir}' is not a directory!")

        # Ignore the train.log file as it can already exist when using multiple devices.
        # TODO(Guarin, 09/24): Fix this by checking that the directory is completely
        # empty at the beginning. For this we have to take multiple devices and repeat
        # calls to this function into account.
        dir_not_empty = any(
            filepath for filepath in out_dir.iterdir() if filepath.name != "train.log"
        )
        if dir_not_empty and not (resume or overwrite):
            raise ValueError(
                f"Output '{out_dir}' is not empty! Set overwrite=True to overwrite the "
                "directory or resume=True to resume training."
            )
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def pretty_format_args(
    args: dict[str, Any], indent: int = 2, width: int = 200, compact: bool = True
) -> str:
    if isinstance(args.get("model"), Module):
        args["model"] = args["model"].__class__.__name__
    if isinstance(args.get("accelerator"), Accelerator):
        args["accelerator"] = args["accelerator"].__class__.__name__
    if isinstance(args.get("strategy"), Strategy):
        args["strategy"] = args["strategy"].__class__.__name__

    return pprint.pformat(args, indent=indent, width=width, compact=compact)


def get_num_workers(num_workers: int | Literal["auto"], num_devices: int) -> int:
    if num_workers == "auto":
        cpu_count = os.cpu_count()
        if cpu_count is None:
            return 8
        return max(((cpu_count - 1) // num_devices), 1)
    return num_workers
