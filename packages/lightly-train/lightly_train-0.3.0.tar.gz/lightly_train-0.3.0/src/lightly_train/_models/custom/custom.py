#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from torch import Tensor
from torch.nn import Module

from lightly_train._models.feature_extractor import FeatureExtractor


class CustomFeatureExtractor(FeatureExtractor):
    def __init__(self, model: Module) -> None:
        super().__init__()

        # TODO: It would be better to not save the full model but only the necessary
        # modules to calculate features. This would save memory and make sure we only
        # train the necessary parameters. Saving all parameters also requires us to
        # use `ddp_find_unused_parameters=True` in the Trainer.
        self._model = model

    @property
    def feature_dim(self) -> int:
        return self._model.num_features()

    def forward_features(self, x: Tensor) -> Tensor:
        return self._model.forward_features(x)

    def forward_pool(self, x: Tensor) -> Tensor:
        features = self._model.forward_pool(x)
        while len(features.shape) < 4:
            features = features.unsqueeze(-1)
        return features
