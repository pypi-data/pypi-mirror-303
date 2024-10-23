#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from lightly_train._methods.dino import DINOArgs
from lightly_train._scaling import ScalingInfo


class TestDINOArgs:
    def test_resolve_auto(self) -> None:
        args = DINOArgs()
        scaling_info = ScalingInfo(dataset_size=20_000)
        args.resolve_auto(scaling_info=scaling_info)
        assert args.output_dim == 2048
        assert args.teacher_temp == 0.02
        assert args.momentum_start == 0.99
        assert not args.has_auto()
