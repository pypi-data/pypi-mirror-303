import torch
import torch.nn as nn
from .utils import StableLogVar as StableLogVar, StableMean as StableMean, kl_normal_mc as kl_normal_mc
from _typeshed import Incomplete

ConvType: Incomplete
NormType: Incomplete
DropoutType: Incomplete

class NormalStochasticBlock(nn.Module):
    transform_p_params: Incomplete
    c_in: Incomplete
    c_out: Incomplete
    c_vars: Incomplete
    conv_dims: Incomplete
    conv_in_p: Incomplete
    conv_in_q: Incomplete
    conv_out: Incomplete
    def __init__(self, c_in: int, c_vars: int, c_out: int, conv_dims: int = 2, kernel: int = 3, transform_p_params: bool = True, vanilla_latent_hw: int = None, restricted_kl: bool = False, use_naive_exponential: bool = False) -> None: ...
    def get_z(self, sampling_distrib: torch.distributions.normal.Normal, forced_latent: torch.Tensor | None, mode_pred: bool, use_uncond_mode: bool) -> torch.Tensor: ...
    def sample_from_q(self, q_params: torch.Tensor, var_clip_max: float) -> torch.Tensor: ...
    def compute_kl_metrics(self, p: torch.distributions.normal.Normal, p_params: torch.Tensor, q: torch.distributions.normal.Normal, q_params: torch.Tensor, mode_pred: bool, analytical_kl: bool, z: torch.Tensor) -> dict[str, torch.Tensor]: ...
    def process_p_params(self, p_params: torch.Tensor, var_clip_max: float) -> tuple[torch.Tensor, torch.Tensor, torch.distributions.normal.Normal]: ...
    def process_q_params(self, q_params: torch.Tensor, var_clip_max: float, allow_oddsizes: bool = False) -> tuple[torch.Tensor, torch.Tensor, torch.distributions.normal.Normal]: ...
    def forward(self, p_params: torch.Tensor, q_params: torch.Tensor | None = None, forced_latent: torch.Tensor | None = None, force_constant_output: bool = False, analytical_kl: bool = False, mode_pred: bool = False, use_uncond_mode: bool = False, var_clip_max: float | None = None) -> tuple[torch.Tensor, dict[str, torch.Tensor]]: ...
