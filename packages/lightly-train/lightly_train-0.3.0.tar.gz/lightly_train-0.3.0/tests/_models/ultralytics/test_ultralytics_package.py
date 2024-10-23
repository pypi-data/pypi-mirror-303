#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import pytest

from lightly_train._models.ultralytics.ultralytics import UltralyticsFeatureExtractor
from lightly_train._models.ultralytics.ultralytics_package import UltralyticsPackage

try:
    from ultralytics import RTDETR, YOLO
except ImportError:
    # We do not use pytest.importorskip on module level because it makes mypy unhappy.
    pytest.skip("ultralytics is not installed", allow_module_level=True)


class TestUltralyticsPackage:
    @pytest.mark.parametrize(
        "model_name, supported",
        [
            ("ultralytics/yolov5s.yaml", True),
            ("ultralytics/yolov5s.pt", False),  # No pretrained checkpoint available.
            ("ultralytics/yolov6s.yaml", True),
            ("ultralytics/yolov6s.pt", False),  # No pretrained checkpoint available.
            ("ultralytics/yolov8s.yaml", True),
            ("ultralytics/yolov8s.pt", True),
            ("ultralytics/yolov10s.pt", False),  # Not yet supported.
        ],
    )
    def test_list_model_names(self, model_name: str, supported: bool) -> None:
        model_names = UltralyticsPackage.list_model_names()
        assert (model_name in model_names) is supported

    def test_is_supported_model__true(self) -> None:
        model = YOLO("yolov8s.yaml")
        assert UltralyticsPackage.is_supported_model(model)

    def test_is_supported_model__false(self) -> None:
        model = RTDETR("rtdetr-l.yaml")
        assert not UltralyticsPackage.is_supported_model(model)

    @pytest.mark.parametrize(
        "model_name",
        ["yolov8s.pt", "yolov8s.yaml"],
    )
    def test_get_model(self, model_name: str) -> None:
        model = UltralyticsPackage.get_model(model_name=model_name)
        assert isinstance(model, YOLO)

    def test_get_feature_extractor_cls(self) -> None:
        model = YOLO("yolov8s.yaml")
        fe_cls = UltralyticsPackage.get_feature_extractor_cls(model=model)
        assert fe_cls == UltralyticsFeatureExtractor
