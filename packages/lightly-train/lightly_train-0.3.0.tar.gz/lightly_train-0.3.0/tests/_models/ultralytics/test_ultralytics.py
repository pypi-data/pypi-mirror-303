#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import pytest
import torch

from lightly_train._models.ultralytics.ultralytics import UltralyticsFeatureExtractor

try:
    from ultralytics import YOLO
except ImportError:
    # We do not use pytest.importorskip on module level because it makes mypy unhappy.
    pytest.skip("ultralytics is not installed", allow_module_level=True)


class TestUltralyticsFeatureExtractor:
    @pytest.mark.parametrize("model_name", ["yolov8s.yaml", "yolov8s.pt"])
    def test_init(self, model_name: str):
        model = YOLO(model_name)
        feature_extractor = UltralyticsFeatureExtractor(model=model)
        for name, param in feature_extractor.named_parameters():
            if ".dfl" in name:
                assert not param.requires_grad, name
            else:
                assert param.requires_grad, name

        for name, module in feature_extractor.named_modules():
            assert module.training, name

    def test_init__freeze(self):
        model = YOLO("yolov8s.yaml")

        # Freeze the first three layers.
        freeze_layers = [0, 1, 2]
        model.model.args["freeze"] = freeze_layers

        feature_extractor = UltralyticsFeatureExtractor(model=model)
        for name, param in feature_extractor.named_parameters():
            if ".dfl" in name or any(f"model.{idx}" in name for idx in freeze_layers):
                assert not param.requires_grad, name
            else:
                assert param.requires_grad, name

    def test_feature_dim(self):
        model = YOLO("yolov8s.yaml")
        feature_extractor = UltralyticsFeatureExtractor(model=model)
        assert feature_extractor.feature_dim == 512

    def test_forward_features(self):
        model = YOLO("yolov8s.yaml")
        feature_extractor = UltralyticsFeatureExtractor(model=model)
        x = torch.rand(1, 3, 224, 224)
        features = feature_extractor.forward_features(x)
        assert features.shape == (1, 512, 7, 7)

    def test_forward_pool(self):
        model = YOLO("yolov8s.yaml")
        feature_extractor = UltralyticsFeatureExtractor(model=model)
        x = torch.rand(1, 512, 7, 7)
        pool = feature_extractor.forward_pool(x)
        assert pool.shape == (1, 512, 1, 1)
