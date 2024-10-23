#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from __future__ import annotations

from typing import Any

from torch.nn import Module

from lightly_train._models.custom.custom import CustomFeatureExtractor
from lightly_train._models.feature_extractor import FeatureExtractor
from lightly_train._models.package import Package


class CustomPackage(Package):
    name = "custom"

    @classmethod
    def list_model_names(cls) -> list[str]:
        return []

    @classmethod
    def is_supported_model(cls, model: Module) -> bool:
        return (
            hasattr(model, "num_features")
            and hasattr(model, "forward_features")
            and hasattr(model, "forward_pool")
        )

    @classmethod
    def get_model(
        cls, model_name: str, model_args: dict[str, Any] | None = None
    ) -> Module:
        raise NotImplementedError()

    @classmethod
    def get_feature_extractor_cls(cls, model: Module) -> type[FeatureExtractor]:
        return CustomFeatureExtractor


# Create singleton instance of the package. The singleton should be used whenever
# possible.
CUSTOM_PACKAGE = CustomPackage()
