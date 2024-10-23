#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import torch

from lightly_train._models.custom.custom import CustomFeatureExtractor

from ...helpers import DummyCustomModel


class TestCustomFeatureExtractor:
    def test_feature_dim(self):
        model = DummyCustomModel(feature_dim=3)
        extractor = CustomFeatureExtractor(model=model)
        assert extractor.feature_dim == 3

    def test_forward_features(self):
        model = DummyCustomModel()
        x = torch.rand(1, 3, 64, 64)

        extractor = CustomFeatureExtractor(model=model)

        y = extractor.forward_features(x)

        assert torch.allclose(y, model.conv(x))

    def test_forward_pool(self):
        model = DummyCustomModel()
        x = torch.rand(1, 3, 3, 3)
        extractor = CustomFeatureExtractor(model=model)
        features = extractor.forward_pool(x)

        assert features.shape == (1, 3, 1, 1)
