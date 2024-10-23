#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from torch import Tensor
from torch.nn import Module


class FeatureExtractor(Module):
    @property
    def feature_dim(self) -> int:
        raise NotImplementedError()

    def forward(self, x: Tensor) -> Tensor:
        """Extracts features and pools them.

        Args:
            x: Inputs with shape (B, C_in, H_in, W_in).

        Returns:
            Pooled features with shape (B, C_out, H_out, W_out). H_out and W_out depend
            on the pooling strategy but are usually 1.
        """
        x = self.forward_features(x)
        x = self.forward_pool(x)
        return x

    def forward_features(self, x: Tensor) -> Tensor:
        """Extracts features.

        Args:
            x: Inputs with shape (B, C_in, H_in, W_in).

        Returns:
            Unpooled features with shape (B, C_out, H_out, W_out). H_out and W_out are
            usually >1.
        """
        raise NotImplementedError()

    def forward_pool(self, x: Tensor) -> Tensor:
        """Pools features, should be called after `forward_features`.

        Args:
            x: Features with shape (B, C_in, H_in, W_in).

        Returns:
            Pooled features with shape (B, C_out, H_out, W_out). H_out and W_out depend
            on the pooling strategy but are usually 1.
        """
        raise NotImplementedError()
