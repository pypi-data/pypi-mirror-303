#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from lightly_train._methods.densecl import DenseCLArgs
from lightly_train._scaling import ScalingInfo


class TestDenseCLArgs:
    def test_resolve_auto(self) -> None:
        args = DenseCLArgs()
        scaling_info = ScalingInfo(dataset_size=20_000)
        args.resolve_auto(scaling_info=scaling_info)
        assert args.memory_bank_size == 4096
        assert not args.has_auto()
