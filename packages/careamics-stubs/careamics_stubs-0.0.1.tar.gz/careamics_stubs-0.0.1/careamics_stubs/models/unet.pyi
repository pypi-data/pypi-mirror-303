import torch
import torch.nn as nn
from ..config.support import SupportedActivation as SupportedActivation
from .activation import get_activation as get_activation
from .layers import Conv_Block as Conv_Block, MaxBlurPool as MaxBlurPool
from _typeshed import Incomplete
from typing import Any

class UnetEncoder(nn.Module):
    pooling: Incomplete
    encoder_blocks: Incomplete
    def __init__(self, conv_dim: int, in_channels: int = 1, depth: int = 3, num_channels_init: int = 64, use_batch_norm: bool = True, dropout: float = 0.0, pool_kernel: int = 2, n2v2: bool = False, groups: int = 1) -> None: ...
    def forward(self, x: torch.Tensor) -> list[torch.Tensor]: ...

class UnetDecoder(nn.Module):
    n2v2: Incomplete
    groups: Incomplete
    bottleneck: Incomplete
    decoder_blocks: Incomplete
    def __init__(self, conv_dim: int, depth: int = 3, num_channels_init: int = 64, use_batch_norm: bool = True, dropout: float = 0.0, n2v2: bool = False, groups: int = 1) -> None: ...
    def forward(self, *features: torch.Tensor) -> torch.Tensor: ...

class UNet(nn.Module):
    encoder: Incomplete
    decoder: Incomplete
    final_conv: Incomplete
    final_activation: Incomplete
    def __init__(self, conv_dims: int, num_classes: int = 1, in_channels: int = 1, depth: int = 3, num_channels_init: int = 64, use_batch_norm: bool = True, dropout: float = 0.0, pool_kernel: int = 2, final_activation: SupportedActivation | str = ..., n2v2: bool = False, independent_channels: bool = True, **kwargs: Any) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...
