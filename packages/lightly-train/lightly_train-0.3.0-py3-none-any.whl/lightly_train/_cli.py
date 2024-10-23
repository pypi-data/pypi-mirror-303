#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from __future__ import annotations

import inspect
import logging
import os
import sys
from typing import Callable

from omegaconf import DictConfig, OmegaConf

import lightly_train
from lightly_train import _logging
from lightly_train._commands import embed, export, extract_video_frames, train
from lightly_train._commands.embed import CLIEmbedConfig
from lightly_train._commands.export import CLIExportConfig
from lightly_train._commands.extract_video_frames import (
    CLIExtractVideoFramesConfig,
)
from lightly_train._commands.train import CLITrainConfig
from lightly_train._logging import LIGHTLY_TRAIN_LOG_LEVEL_ENV_VAR
from lightly_train._models import package_helpers
from lightly_train.errors import ConfigError

logger = logging.getLogger(__name__)

_HELP_COMMANDS = {"help", "--help", "-h"}
_HELP_MSG = """
    Commands:
        lightly-train train                 Train model with self-supervised learning.
        lightly-train export                Export model from checkpoint.
        lightly-train embed                 Embed images using a trained model.
        lightly-train list_models           List supported models for training.
        lightly-train list_methods          List supported methods for training.
        lightly-train extract_video_frames  Extract frames from videos using ffmpeg.
        lightly-train help                  Show help message.

    Run `lightly-train <command> help` for more information on a specific command.

    Optional arguments:
        -v, --verbose  Run the command in verbose mode for detailed output.
    """

_train_cfg = CLITrainConfig(out="", data="", model="")
_TRAIN_HELP_MSG = f"""
    Train a model with self-supervised learning.

    The training process can be monitored with TensorBoard (requires 
    `pip install lightly-train[tensorboard]`):

        tensorboard --logdir out


    After training, the model checkpoint is saved to `out/checkpoints/last.ckpt` and can
    be exported to different formats using the `lightly-train export` command.

    Usage:
        lightly-train train [options]

    Options:
        out (str, required):
            Output directory to save logs, checkpoints, and other artifacts.
        data (str, required):
            Path to a directory containing images.
        model (str, required):
            Model name for training. For example 'torchvision/resnet50'.
            Run `lightly-train list_models` to see all supported models.
        method (str, required):
            Method name for training. For example 'simclr'. Default: {_train_cfg.method}
            Run `lightly-train list_methods` to see all supported methods.
        method_args (dict):
            Arguments for the self-supervised learning method. The available arguments
            depend on the `method` parameter.
        embed_dim (int):
            Embedding dimension. Set this if you want to train an embedding model with
            a specific dimension. By default, the output dimension of `model` is used.
        epochs (int):
            Number of training epochs. Default: {_train_cfg.epochs}
        batch_size (int):
            Global batch size. Default: {_train_cfg.batch_size}
        num_workers (int | "auto"):
            Number of workers for the dataloader per device/GPU. 'auto' automatically  
            sets the number of workers based on the available CPU cores. Default:
            {_train_cfg.num_workers}
        devices (int):
            Number of devices/GPUs to use for training. By default, all available
            devices are used.
        num_nodes (int):
            Number of nodes for distributed training. Default: {_train_cfg.num_nodes}
        resume (bool):
            Resume training from the latest checkpoint. Default: {_train_cfg.resume}
        overwrite (bool):
            Overwrite the output directory if it exists. Warning, this might overwrite
            existing files in the directory! Default: {_train_cfg.overwrite}
        accelerator (str):
            Hardware accelerator. Can be one of ['cpu', 'gpu', 'tpu', 'ipu', 'hpu',
            'mps', 'auto']. 'auto' automatically selects the best acccelerator
            available. Default: {_train_cfg.accelerator}
            For details, see: https://pytorch-lightning.readthedocs.io/en/stable/accelerators.html
        strategy (str):
            Training strategy. For example 'ddp' or 'auto'. 'auto' automatically
            selects the best strategy available. Default: {_train_cfg.strategy}
            For details, see: https://lightning.ai/docs/pytorch/stable/common/trainer.html#strategy
        precision (str):
            Training precision. Select '16-mixed' for mixed 16-bit precision, '32-true'
            for full 32-bit precision, or 'bf16-mixed' for mixed bfloat16 precision.
            Default: {_train_cfg.precision}
            For details, see: https://lightning.ai/docs/pytorch/stable/common/trainer.html#precision
        seed (int):
            Random seed for reproducibility. Default: {_train_cfg.seed}
        loggers (dict):
            Loggers for training. Either null or a dictionary of logger names to either
            null or a dictionary of logger arguments. Null uses the default loggers.
            To disable a logger, set it to null: `loggers.tensorboard=null`.
            To configure a logger, pass the respective arguments:
            `loggers.wandb.project="my_project"`.
            Default: null
        callbacks (dict):
            Callbacks fo training. Either null or a dictionary of callback names to
            either null or a dictionary of callback arguments. Null uses the default
            callbacks. To disable a callback, set it to null:
            `callbacks.model_checkpoint=null`. To configure a callback, pass the
            respective arguments: `callbacks.model_checkpoint.every_n_epochs=5`.
            Default: null
        optim_args (dict):
            Arguments for AdamW optimizer. Available arguments are:
            - lr (float)
            - betas (tuple[float, float])
            - weight_decay (float)
        transform_args (dict):
            Additional arguments for the image transform. The available arguments depend
            on the `method` parameter. For example, if `method=simclr`, the arguments
            are passed to `lightly.transforms.SimCLRTransform`. See the lightly
            transforms documentation for available arguments:
            https://docs.lightly.ai/self-supervised-learning/lightly.transforms.html
        loader_args (dict):
            Additional arguments for the PyTorch DataLoader.
        trainer_args (dict):
            Additional arguments for the PyTorch Lightning Trainer.
        model_args (dict):
            Additional arguments for the model. The available arguments depend on the
            the `model` parameter.

    Optional arguments:
        -v, --verbose  Run the command in verbose mode for detailed output.

    Examples:
    # Train a ResNet-18 model with SimCLR on ImageNet
    lightly-train train out=out data=imagenet/train model=torchvision/resnet18 method=simclr

    # Train a ConvNext embedding model with DINO
    lightly-train train out=out data=imagenet/train model=torchvision/convnext_small \\
        method=dino embed_dim=128 epochs=300 batch_size=64 precision=16-mixed \\
        transform_args.global_crop_size=178 optim_args.lr=0.01 \\
        optim_args.betas="[0.9, 0.999]"
"""
_export_cfg = CLIExportConfig(checkpoint="", out="", part="", format="")
_EXPORT_HELP_MSG = f"""
    Export a model from a checkpoint.

    Usage:
        lightly-train export [options]

    Options:
        out (str, required):
            Path where the exported model will be saved.
        checkpoint (str, required):
            Path to the LightlyTrain checkpoint file to export the model from. The
            location of the checkpoint depends on the train command. If training was run
            with `out="my_output_dir"`, then the last LightlyTrain checkpoint is saved
            to `my_output_dir/checkpoints/last.ckpt`.
        part (str, required):
            Part of the model to export. Valid options are 'model' and 'embedding_model'.
            'model' exports the entire model, while 'embedding_model' exports only the
            embedding part of the model.
        format (str, required):
            Format to save the model in. Valid options are 'torch_model' and
            'torch_state_dict'. 'torch_model' saves the model as a torch module which
            can be loaded with `model = torch.load(out)`. This requires that the same
            LightlyTrain version is installed when the model is exported and when it is
            loaded again. 'torch_state_dict' saves the model's state dict which can be
            loaded with `model.load_state_dict(torch.load(out))`. This is more flexible
            and can be used to load the model with different LightlyTrain versions but
            requires the model to already be instantiated.
        overwrite (bool):
            Overwrite the output file if it already exists. Default: {_export_cfg.overwrite}

    Optional arguments:
        -v, --verbose  Run the command in verbose mode for detailed output.

    Examples:
    # Export the state dict of the model
    lightly-train export checkpoint=out/checkpoints/last.ckpt out=out/model.pth \\
        part=model format=torch_state_dict

    # Export the embedding model as a torch module
    lightly-train export checkpoint=out/checkpoints/last.ckpt out=out/embedding_model.pth \\
        part=embedding_model format=torch_model
"""
_embed_cfg = CLIEmbedConfig(out="", data="", checkpoint="", format="")
_EMBED_HELP_MSG = f"""
    Embed images from a model checkpoint.

    Usage:
        lightly-train embed [options]

    Options:
        out (str, required):
            Filepath where the embeddings will be saved. For example "embeddings.csv".
        data (str, required):
            Directory containing the images to embed.
        checkpoint (str, required):
            Path to the LightlyTrain checkpoint file used for embedding. The location of
            the checkpoint depends on the train command. If training was run with
            `out="my_output_dir"`, then the last LightlyTrain checkpoint is saved to
            `my_output_dir/checkpoints/last.ckpt`.
        format (str, required):
            Format of the embeddings. Supported formats are ['csv', 'lightly_csv',
            'torch']. Use 'lightly_csv' if you want to use the embeddings as custom
            embeddings with the Lightly Worker. See the relevant docs for more
            information: https://docs.lightly.ai/docs/custom-embeddings
            Use `torch.load(out)` to load the embeddings if you choose 'torch' format.
        image_size (int or [int, int]):
            Size to which the images are resized before embedding. If a single integer
            is provided, the image is resized to a square with the given side length.
            If a [height, width] list is provided, the image is resized to the given
            height and width. Note that not all models support all image sizes.
        batch_size (int):
            Number of images per batch.
        num_workers (int | "auto"):
            Number of workers for the dataloader. 'auto' automatically  sets the number
            of workers based on the available CPU cores. Default: {_embed_cfg.num_workers}
        accelerator (str):
            Hardware accelerator. Can be one of ['cpu', 'gpu', 'tpu', 'ipu', 'hpu',
            'mps', 'auto']. 'auto' will automatically select the best accelerator
            available. For details, see:
            https://lightning.ai/docs/pytorch/stable/common/trainer.html#accelerator
        overwrite (bool):
            Overwrite the output file if it already exists.

    Optional arguments:
        -v, --verbose  Run the command in verbose mode for detailed output.

    Examples:
    # Embed images from a model checkpoint
    lightly-train embed out=embeddings.csv data=images checkpoint=out/checkpoints/last.ckpt \\
        format=csv

    # Create custom embeddings for the Lightly Worker
    lightly-train embed out=embeddings.csv data=images checkpoint=out/checkpoints/last.ckpt \\
        format=lightly_csv

    # Embed images with a different image size
    lightly-train embed out=embeddings.csv data=images checkpoint=out/checkpoints/last.ckpt \\
        format=csv image_size="[448, 672]"
"""

_extract_cfg = CLIExtractVideoFramesConfig(data="", out="")
_EXTRACT_VIDEO_FRAMES_HELP_MSG = f"""
    Extract frames from videos using ffmpeg.

    Directly calls ffmpeg via subprocess. This is the most performant option. Requires
    ffmpeg to be installed on the system.
    Installation of ffmpeg:
        - {extract_video_frames.FFMPEG_INSTALLATION_EXAMPLES[0]}
        - {extract_video_frames.FFMPEG_INSTALLATION_EXAMPLES[1]}
        - {extract_video_frames.FFMPEG_INSTALLATION_EXAMPLES[2]}

    Usage:
        lightly-train extract_video_frames [options]

    Options:
        data (str, required):
            Path to a directory containing video files.
        out (str, required):
            Output directory to save the extracted frames.
        overwrite (bool):
            If True, existing frames are overwritten. If false, the out directory must
            be empty. Default: {_extract_cfg.overwrite}
        frame_filename_format (str):
            Filename format for the extracted frames, passed as it is to ffmpeg.
            Default: "{_extract_cfg.frame_filename_format}" for extracting frames as jpg
            files and with the 9-digit frame number as filename.
        num_workers (int | "auto"):
            Number of parallel calls to ffmpeg. 'auto' automatically sets the number of
            workers based on the available CPU cores. Default: {_extract_cfg.num_workers}

    Optional arguments:
        -v, --verbose  Run the command in verbose mode for detailed output.

    Examples:
    # Extract frames from videos
    lightly-train extract_video_frames data=videos out=frames

    # Extract frames with a custom filename format
    lightly-train extract_video_frames data=videos out=frames frame_filename_format="%04d.jpg"

    # Extract frames using 2 parallel calls to ffmpeg
    lightly-train extract_video_frames data=videos out=frames frame_filename_format="%04d.jpg"
"""


_VERBOSE_FLAGS = ["-v", "--verbose"]


def cli(config: DictConfig) -> None:
    keys = list(config.keys())

    # Check if the user wants to run the command in verbose mode.
    # Any of the following will enable verbose mode: -v, --verbose
    if any(flag in keys for flag in _VERBOSE_FLAGS):
        os.environ[LIGHTLY_TRAIN_LOG_LEVEL_ENV_VAR] = str(logging.DEBUG)
        config = OmegaConf.create(
            {k: v for k, v in config.items() if k not in _VERBOSE_FLAGS}
        )
    _logging.set_up_console_logging()

    if config.is_empty():
        _show_help()
        return

    # First argument after lightly_train is the command. For example `lightly-train train ...`
    command = str(keys[0]).lower()
    help_if_config_empty = True
    if command in _HELP_COMMANDS:
        _show_help()
        return
    elif command == "train":
        command_fn = train.train_from_dictconfig
        help_msg = _TRAIN_HELP_MSG
    elif command == "export":
        command_fn = export.export_from_dictconfig
        help_msg = _EXPORT_HELP_MSG
    elif command == "embed":
        command_fn = embed.embed_from_dictconfig
        help_msg = _EMBED_HELP_MSG
    elif command == "extract_video_frames":
        command_fn = extract_video_frames.extract_video_frames_from_dictconfig
        help_msg = _EXTRACT_VIDEO_FRAMES_HELP_MSG
    elif command == "list_models":
        command_fn = _list_models
        help_msg = ""
        help_if_config_empty = False
    elif command == "list_methods":
        command_fn = _list_methods
        help_msg = ""
        help_if_config_empty = False
    else:
        _show_invalid_command_help(command=command)
        sys.exit(1)

    config.pop(command)
    _run_command_fn(
        command_fn=command_fn,
        config=config,
        help_msg=help_msg,
        help_if_config_empty=help_if_config_empty,
    )


def _cli_entrypoint() -> None:
    # Entrypoint to CLI used in pyproject.toml
    cli(config=OmegaConf.from_cli())


def _run_command_fn(
    command_fn: Callable[[DictConfig], None],
    config: DictConfig,
    help_msg: str,
    help_if_config_empty: bool,
) -> None:
    """Runs a subcommand function with the given config.

    Args:
        command_fn:
            The function to run.
        config:
            Config passed to `command_fn`.
        help_msg:
            The help message to display if a help command is found in the config. For
            example in `lightly-train train help`.
        help_if_config_empty:
            If yes, then show the help message if the config is empty. This is useful
            if a user runs `lightly-train train` without any arguments.
    """
    if _is_help_command_in_config(config) or (
        config.is_empty() and help_if_config_empty
    ):
        _show_msg(help_msg)
        return

    try:
        command_fn(config)
    except ConfigError as ex:
        logger.error(ex)
        raise ex from None  # Shorten stacktrace
    except Exception as ex:
        logger.error(ex)
        raise ex from None  # Shorten stacktrace


def _list_models(config: DictConfig) -> None:
    lines = [f"    {model}" for model in package_helpers.list_model_names()]
    logger.info("\n".join(lines))


def _list_methods(config: DictConfig) -> None:
    lines = [f"    {method}" for method in lightly_train.list_methods()]
    logger.info("\n".join(lines))


def _is_help_command_in_config(config: DictConfig) -> bool:
    return any(help_command in config for help_command in _HELP_COMMANDS)


def _show_help() -> None:
    _show_msg(_HELP_MSG)


def _show_invalid_command_help(command: str) -> None:
    msg = _format_msg(
        f"""
        Unknown command '{command}':
            lightly-train {command}
        """
    )
    msg += "\n"
    msg += _format_msg(_HELP_MSG.replace("Commands:", "Valid commands are:"))
    _show_msg(msg)


def _show_msg(msg: str) -> None:
    logger.info(_format_msg(msg))


def _format_msg(msg: str) -> str:
    # Inspect.cleandoc removes leading whitespaces from messages. This helps with
    # multiline strings.
    return inspect.cleandoc(msg)
