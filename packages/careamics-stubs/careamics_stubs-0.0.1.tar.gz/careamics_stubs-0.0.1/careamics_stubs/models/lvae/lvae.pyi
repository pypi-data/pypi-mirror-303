import torch
import torch.nn as nn
from ..activation import get_activation as get_activation
from .layers import BottomUpDeterministicResBlock as BottomUpDeterministicResBlock, BottomUpLayer as BottomUpLayer, GateLayer as GateLayer, TopDownDeterministicResBlock as TopDownDeterministicResBlock, TopDownLayer as TopDownLayer
from .utils import Interpolate as Interpolate, ModelType as ModelType, crop_img_tensor as crop_img_tensor
from _typeshed import Incomplete
from careamics.config.architectures import register_model as register_model
from collections.abc import Iterable

class LadderVAE(nn.Module):
    image_size: Incomplete
    target_ch: Incomplete
    encoder_conv_strides: Incomplete
    decoder_conv_strides: Incomplete
    z_dims: Incomplete
    encoder_n_filters: Incomplete
    decoder_n_filters: Incomplete
    encoder_dropout: Incomplete
    decoder_dropout: Incomplete
    nonlin: Incomplete
    predict_logvar: Incomplete
    analytical_kl: Incomplete
    model_type: Incomplete
    encoder_blocks_per_layer: int
    decoder_blocks_per_layer: int
    bottomup_batchnorm: bool
    topdown_batchnorm: bool
    topdown_conv2d_bias: bool
    gated: bool
    encoder_res_block_kernel: int
    decoder_res_block_kernel: int
    encoder_res_block_skip_padding: bool
    decoder_res_block_skip_padding: bool
    merge_type: str
    no_initial_downscaling: bool
    skip_bottomk_buvalues: int
    stochastic_skip: bool
    learn_top_prior: bool
    res_block_type: str
    mode_pred: bool
    logvar_lowerbound: int
    enable_multiscale: Incomplete
    multiscale_retain_spatial_dims: bool
    multiscale_lowres_separate_branch: bool
    multiscale_decoder_retain_spatial_dims: Incomplete
    n_layers: Incomplete
    color_ch: int
    normalized_input: bool
    mixed_rec_w: int
    nbr_consistency_w: int
    downsample: Incomplete
    overall_downscale_factor: Incomplete
    encoder_conv_op: Incomplete
    decoder_conv_op: Incomplete
    first_bottom_up: Incomplete
    lowres_first_bottom_ups: Incomplete
    bottom_up_layers: Incomplete
    top_down_layers: Incomplete
    final_top_down: Incomplete
    output_layer: Incomplete
    def __init__(self, input_shape: int, output_channels: int, multiscale_count: int, z_dims: list[int], encoder_n_filters: int, decoder_n_filters: int, encoder_conv_strides: list[int], decoder_conv_strides: list[int], encoder_dropout: float, decoder_dropout: float, nonlinearity: str, predict_logvar: bool, analytical_kl: bool) -> None: ...
    def create_first_bottom_up(self, init_stride: int, num_res_blocks: int = 1) -> nn.Sequential: ...
    def create_bottom_up_layers(self, lowres_separate_branch: bool) -> nn.ModuleList: ...
    def create_top_down_layers(self) -> nn.ModuleList: ...
    def create_final_topdown_layer(self, upsample: bool) -> nn.Sequential: ...
    def bottomup_pass(self, inp: torch.Tensor) -> list[torch.Tensor]: ...
    def topdown_pass(self, bu_values: torch.Tensor | None = None, n_img_prior: torch.Tensor | None = None, constant_layers: Iterable[int] | None = None, forced_latent: list[torch.Tensor] | None = None, top_down_layers: nn.ModuleList | None = None, final_top_down_layer: nn.Sequential | None = None) -> tuple[torch.Tensor, dict[str, torch.Tensor]]: ...
    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, dict[str, torch.Tensor]]: ...
    def get_padded_size(self, size): ...
    def get_latent_spatial_size(self, level_idx: int): ...
    def get_top_prior_param_shape(self, n_imgs: int = 1): ...
