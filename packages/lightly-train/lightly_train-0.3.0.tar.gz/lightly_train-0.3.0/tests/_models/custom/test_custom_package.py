#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from pytest_mock import MockerFixture

from lightly_train._models.custom.custom_package import CustomPackage

from ...helpers import DummyCustomModel


class TestCustomPackage:
    def test_is_supported_model(self) -> None:
        assert CustomPackage.is_supported_model(DummyCustomModel())

    def test_is_supported_model__no_num_features(self, mocker: MockerFixture) -> None:
        model = DummyCustomModel()
        mocker.patch.object(
            DummyCustomModel, "num_features", new_callable=mocker.PropertyMock
        )
        del DummyCustomModel.num_features
        assert not CustomPackage.is_supported_model(model)

    def test_is_supported_model__no_forward_features(
        self, mocker: MockerFixture
    ) -> None:
        model = DummyCustomModel()
        mocker.patch.object(DummyCustomModel, "forward_features", new=None)
        del DummyCustomModel.forward_features
        assert not CustomPackage.is_supported_model(model)

    def test_is_custom_model__no_forward_pool(self, mocker: MockerFixture) -> None:
        model = DummyCustomModel()
        mocker.patch.object(DummyCustomModel, "forward_pool", new=None)
        del DummyCustomModel.forward_pool
        assert not CustomPackage.is_supported_model(model)
