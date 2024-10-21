import torch
import torch.nn as nn
from _typeshed import Incomplete
from collections.abc import Iterable

def torch_nanmean(inp): ...
def compute_batch_mean(x): ...
def power_of_2(self, x): ...

class Enum:
    @classmethod
    def name(cls, enum_type): ...
    @classmethod
    def contains(cls, enum_type): ...
    @classmethod
    def from_name(cls, enum_type_str): ...

class LossType(Enum):
    Elbo: int
    ElboWithCritic: int
    ElboMixedReconstruction: int
    MSE: int
    ElboWithNbrConsistency: int
    ElboSemiSupMixedReconstruction: int
    ElboCL: int
    ElboRestrictedReconstruction: int
    DenoiSplitMuSplit: int

class ModelType(Enum):
    LadderVae: int
    LadderVaeTwinDecoder: int
    LadderVAECritic: int
    LadderVaeSepVampprior: int
    LadderVaeSepEncoder: int
    LadderVAEMultiTarget: int
    LadderVaeSepEncoderSingleOptim: int
    UNet: int
    BraveNet: int
    LadderVaeStitch: int
    LadderVaeSemiSupervised: int
    LadderVaeStitch2Stage: int
    LadderVaeMixedRecons: int
    LadderVaeCL: int
    LadderVaeTwoDataSet: int
    LadderVaeTwoDatasetMultiBranch: int
    LadderVaeTwoDatasetMultiOptim: int
    LVaeDeepEncoderIntensityAug: int
    AutoRegresiveLadderVAE: int
    LadderVAEInterleavedOptimization: int
    Denoiser: int
    DenoiserSplitter: int
    SplitterDenoiser: int
    LadderVAERestrictedReconstruction: int
    LadderVAETwoDataSetRestRecon: int
    LadderVAETwoDataSetFinetuning: int

def pad_img_tensor(x: torch.Tensor, size: Iterable[int]) -> torch.Tensor: ...
def crop_img_tensor(x, size) -> torch.Tensor: ...

class StableExponential:
    def __init__(self, tensor) -> None: ...
    def posneg_separation(self, tensor): ...
    def exp(self): ...
    def log(self): ...

class StableLogVar:
    def __init__(self, logvar, enable_stable: bool = True, var_eps: float = 1e-06) -> None: ...
    def get(self): ...
    def get_var(self): ...
    def get_std(self): ...
    def centercrop_to_size(self, size) -> None: ...

class StableMean:
    def __init__(self, mean) -> None: ...
    def get(self): ...
    def centercrop_to_size(self, size) -> None: ...

def allow_numpy(func): ...

class Interpolate(nn.Module):
    size: Incomplete
    scale: Incomplete
    mode: Incomplete
    align_corners: Incomplete
    def __init__(self, size: Incomplete | None = None, scale: Incomplete | None = None, mode: str = 'bilinear', align_corners: bool = False) -> None: ...
    def forward(self, x): ...

def kl_normal_mc(z, p_mulv, q_mulv): ...
def free_bits_kl(kl: torch.Tensor, free_bits: float, batch_average: bool = False, eps: float = 1e-06) -> torch.Tensor: ...
