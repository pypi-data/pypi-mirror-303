#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from torch import Tensor
from torch.nn import AdaptiveAvgPool2d, Sequential

from lightly_train._models.feature_extractor import FeatureExtractor

if TYPE_CHECKING:
    from ultralytics import YOLO

logger = logging.getLogger(__name__)


class UltralyticsFeatureExtractor(FeatureExtractor):
    def __init__(self, model: YOLO) -> None:
        super().__init__()
        _enable_gradients(model=model)
        # Set model to training mode. This is necessary for Ultralytics pre-trained
        # models as they are loaded in eval mode by default.
        model.model.train()
        self._model = model
        self._backbone, self._feature_dim = _get_backbone(model)
        self._pool = AdaptiveAvgPool2d((1, 1))

    @property
    def feature_dim(self) -> int:
        return self._feature_dim

    def forward_features(self, x: Tensor) -> Tensor:
        return self._backbone(x)

    def forward_pool(self, x: Tensor) -> Tensor:
        return self._pool(x)


def _get_backbone(model: YOLO) -> tuple[Sequential, int]:
    """Extracts the backbone and feature dimension from the model.

    Ultralytics doesn't provide a way to get the backbone of the model. All layers
    are stored in a Sequential object. We create the backbone by finding the last
    layer of the backbone. This is the SPPF layer for yolov8 models.
    """
    from ultralytics.nn.modules.block import SPPF

    # Ultralytics stores the actual model in YOLO.model.model
    seq = model.model.model
    assert isinstance(seq, Sequential)
    for i, module in enumerate(seq):
        # SPPF is the last layer of the backbone.
        if isinstance(module, SPPF):
            backbone = seq[: i + 1]
            # Take output channels of the last convolutional layer.
            feature_dim = module.cv2.conv.out_channels
            return backbone, feature_dim
    raise RuntimeError(f"Could not find SSPF module in model {type(model)}")


def _enable_gradients(model: YOLO) -> None:
    """Enables gradients for parameters in the model.

    Ultralytics disables by default gradients for models loaded from a checkpoint
    and enables gradients for models loaded from a config file. This function enables
    gradients for training. It respects the 'freeze' argument in the model's config
    if it exists.
    """
    # The logic of the function follows the one in the original Ultralytics code:
    # https://github.com/ultralytics/ultralytics/blob/6dcc4a0610bf445212253fb51b24e29429a2bcc3/ultralytics/engine/trainer.py#L238C11-L258
    freeze_names = [".dfl"]
    if model.model is not None and model.model.args is not None:
        freeze = model.model.args.get("freeze")
        freeze_list = (
            freeze
            if isinstance(freeze, list)
            else range(freeze)
            if isinstance(freeze, int)
            else []
        )
        freeze_names.extend([f"model.{x}" for x in freeze_list])
    logger.debug(f"Freezing parameters with names {freeze_names}")
    for name, param in model.named_parameters():
        if any(freeze_name in name for freeze_name in freeze_names):
            logger.info(f"Disabling gradients for parameter '{name}'")
            param.requires_grad = False
        elif not param.requires_grad:
            logger.info(f"Enabling gradients for parameter '{name}'")
            param.requires_grad = True
