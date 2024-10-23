#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from __future__ import annotations

import pytest
from torch.nn import Linear

from lightly_train._optim import optimizer
from lightly_train._optim.adamw_args import AdamWArgs
from lightly_train._optim.optimizer_type import OptimizerType
from lightly_train._optim.trainable_modules import TrainableModules


def test_get_optimizer_type() -> None:
    assert optimizer.get_optimizer_type(OptimizerType.ADAMW) == OptimizerType.ADAMW
    assert optimizer.get_optimizer_type("adamw") == OptimizerType.ADAMW


def test_get_optimizer_type__invalid() -> None:
    with pytest.raises(ValueError) as ex_info:
        optimizer.get_optimizer_type("invalid")

    # Check that valid optimizer type is in the error message
    assert "adamw" in str(ex_info.value)


def test_get_optimizer() -> None:
    linear1 = Linear(in_features=1, out_features=1)
    linear2 = Linear(in_features=1, out_features=2)
    optim_args = AdamWArgs()
    optim = optimizer.get_optimizer(
        optim_args=optim_args,
        trainable_modules=TrainableModules(
            modules=[linear1],
            modules_no_weight_decay=[linear2],
        ),
        lr_scale=2.0,
    )
    pg0 = optim.param_groups[0]
    assert pg0["name"] == "params"
    # Bias parameters are excluded from weight decay.
    assert pg0["params"] == [linear1.weight]
    assert pg0["weight_decay"] == optim_args.weight_decay
    assert pg0["lr"] == optim_args.lr * 2

    pg1 = optim.param_groups[1]
    assert pg1["name"] == "params_no_weight_decay"
    assert pg1["params"] == [linear1.bias, linear2.weight, linear2.bias]
    assert pg1["weight_decay"] == 0.0
    assert pg1["lr"] == optim_args.lr * 2
