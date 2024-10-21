import torch
import torch.nn as nn
from _typeshed import Incomplete

class Conv_Block(nn.Module):
    use_batch_norm: Incomplete
    conv1: Incomplete
    conv2: Incomplete
    batch_norm1: Incomplete
    batch_norm2: Incomplete
    dropout: Incomplete
    activation: Incomplete
    def __init__(self, conv_dim: int, in_channels: int, out_channels: int, intermediate_channel_multiplier: int = 1, stride: int = 1, padding: int = 1, bias: bool = True, groups: int = 1, activation: str = 'ReLU', dropout_perc: float = 0, use_batch_norm: bool = False) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

def get_pascal_kernel_1d(kernel_size: int, norm: bool = False, *, device: torch.device | None = None, dtype: torch.dtype | None = None) -> torch.Tensor: ...

class MaxBlurPool(nn.Module):
    dim: Incomplete
    kernel_size: Incomplete
    stride: Incomplete
    max_pool_size: Incomplete
    ceil_mode: Incomplete
    kernel: Incomplete
    def __init__(self, dim: int, kernel_size: tuple[int, int] | int, stride: int = 2, max_pool_size: int = 2, ceil_mode: bool = False) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...
