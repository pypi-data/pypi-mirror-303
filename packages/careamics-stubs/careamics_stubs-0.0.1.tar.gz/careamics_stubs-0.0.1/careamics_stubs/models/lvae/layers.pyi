import torch
import torch.nn as nn
from .stochastic import NormalStochasticBlock as NormalStochasticBlock
from .utils import crop_img_tensor as crop_img_tensor, pad_img_tensor as pad_img_tensor
from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Callable, Literal

ConvType: Incomplete
NormType: Incomplete
DropoutType: Incomplete

class ResidualBlock(nn.Module):
    default_kernel_size: Incomplete
    gated: Incomplete
    block: Incomplete
    def __init__(self, channels: int, nonlin: Callable, conv_strides: tuple[int] = (2, 2), kernel: int | Iterable[int] | None = None, groups: int = 1, batchnorm: bool = True, block_type: str = None, dropout: float = None, gated: bool = None, conv2d_bias: bool = True) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class ResidualGatedBlock(ResidualBlock):
    def __init__(self, *args, **kwargs) -> None: ...

class GateLayer(nn.Module):
    conv: Incomplete
    nonlin: Incomplete
    def __init__(self, channels: int, conv_strides: tuple[int] = (2, 2), kernel_size: int = 3, nonlin: Callable = ...) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class ResBlockWithResampling(nn.Module):
    pre_conv: Incomplete
    res: Incomplete
    post_conv: Incomplete
    def __init__(self, mode: Literal['top-down', 'bottom-up'], c_in: int, c_out: int, conv_strides: tuple[int], min_inner_channels: int | None = None, nonlin: Callable = ..., resample: bool = False, res_block_kernel: int | Iterable[int] | None = None, groups: int = 1, batchnorm: bool = True, res_block_type: str | None = None, dropout: float | None = None, gated: bool | None = None, conv2d_bias: bool = True) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class TopDownDeterministicResBlock(ResBlockWithResampling):
    def __init__(self, *args, upsample: bool = False, **kwargs) -> None: ...

class BottomUpDeterministicResBlock(ResBlockWithResampling):
    def __init__(self, *args, downsample: bool = False, **kwargs) -> None: ...

class BottomUpLayer(nn.Module):
    enable_multiscale: Incomplete
    lowres_separate_branch: Incomplete
    multiscale_retain_spatial_dims: Incomplete
    multiscale_lowres_size_factor: Incomplete
    decoder_retain_spatial_dims: Incomplete
    output_expected_shape: Incomplete
    net_downsized: Incomplete
    net: Incomplete
    lowres_net: Incomplete
    def __init__(self, n_res_blocks: int, n_filters: int, conv_strides: tuple[int] = (2, 2), downsampling_steps: int = 0, nonlin: Callable | None = None, batchnorm: bool = True, dropout: float | None = None, res_block_type: str | None = None, res_block_kernel: int | None = None, gated: bool | None = None, enable_multiscale: bool = False, multiscale_lowres_size_factor: int | None = None, lowres_separate_branch: bool = False, multiscale_retain_spatial_dims: bool = False, decoder_retain_spatial_dims: bool = False, output_expected_shape: Iterable[int] | None = None) -> None: ...
    def forward(self, x: torch.Tensor, lowres_x: torch.Tensor | None = None) -> tuple[torch.Tensor, torch.Tensor]: ...

class MergeLayer(nn.Module):
    conv_layer: Incomplete
    layer: Incomplete
    def __init__(self, merge_type: Literal['linear', 'residual', 'residual_ungated'], channels: int | Iterable[int], conv_strides: tuple[int] = (2, 2), nonlin: Callable = ..., batchnorm: bool = True, dropout: float | None = None, res_block_type: str | None = None, res_block_kernel: int | None = None, conv2d_bias: bool | None = True) -> None: ...
    def forward(self, *args) -> torch.Tensor: ...

class MergeLowRes(MergeLayer):
    retain_spatial_dims: Incomplete
    multiscale_lowres_size_factor: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def forward(self, latent: torch.Tensor, lowres: torch.Tensor) -> torch.Tensor: ...

class SkipConnectionMerger(MergeLayer):
    def __init__(self, nonlin: Callable, channels: int | Iterable[int], batchnorm: bool, dropout: float, res_block_type: str, conv_strides: tuple[int] = (2, 2), merge_type: Literal['linear', 'residual', 'residual_ungated'] = 'residual', conv2d_bias: bool = True, res_block_kernel: int | None = None) -> None: ...

class TopDownLayer(nn.Module):
    is_top_layer: Incomplete
    z_dim: Incomplete
    stochastic_skip: Incomplete
    learn_top_prior: Incomplete
    analytical_kl: Incomplete
    retain_spatial_dims: Incomplete
    input_image_shape: Incomplete
    latent_shape: Incomplete
    normalize_latent_factor: Incomplete
    top_prior_params: Incomplete
    deterministic_block: Incomplete
    stochastic: Incomplete
    merge: Incomplete
    skip_connection_merger: Incomplete
    def __init__(self, z_dim: int, n_res_blocks: int, n_filters: int, conv_strides: tuple[int], is_top_layer: bool = False, upsampling_steps: int | None = None, nonlin: Callable | None = None, merge_type: Literal['linear', 'residual', 'residual_ungated'] | None = None, batchnorm: bool = True, dropout: float | None = None, stochastic_skip: bool = False, res_block_type: str | None = None, res_block_kernel: int | None = None, groups: int = 1, gated: bool | None = None, learn_top_prior: bool = False, top_prior_param_shape: Iterable[int] | None = None, analytical_kl: bool = False, retain_spatial_dims: bool = False, restricted_kl: bool = False, vanilla_latent_hw: Iterable[int] | None = None, input_image_shape: tuple[int, int] | None = None, normalize_latent_factor: float = 1.0, conv2d_bias: bool = True, stochastic_use_naive_exponential: bool = False) -> None: ...
    def sample_from_q(self, input_: torch.Tensor, bu_value: torch.Tensor, var_clip_max: float | None = None, mask: torch.Tensor = None) -> torch.Tensor: ...
    def get_p_params(self, input_: torch.Tensor, n_img_prior: int) -> torch.Tensor: ...
    def forward(self, input_: torch.Tensor | None = None, skip_connection_input: torch.Tensor | None = None, inference_mode: bool = False, bu_value: torch.Tensor | None = None, n_img_prior: int | None = None, forced_latent: torch.Tensor | None = None, force_constant_output: bool = False, mode_pred: bool = False, use_uncond_mode: bool = False, var_clip_max: float | None = None) -> tuple[torch.Tensor, dict[str, torch.Tensor]]: ...
