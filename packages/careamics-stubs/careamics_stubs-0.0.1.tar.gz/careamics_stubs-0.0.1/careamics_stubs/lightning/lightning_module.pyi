import pytorch_lightning as L
from _typeshed import Incomplete
from careamics.config import FCNAlgorithmConfig as FCNAlgorithmConfig, VAEAlgorithmConfig as VAEAlgorithmConfig
from careamics.config.likelihood_model import NMLikelihoodConfig as NMLikelihoodConfig
from careamics.config.support import SupportedAlgorithm as SupportedAlgorithm, SupportedArchitecture as SupportedArchitecture, SupportedLoss as SupportedLoss, SupportedOptimizer as SupportedOptimizer, SupportedScheduler as SupportedScheduler
from careamics.losses import loss_factory as loss_factory
from careamics.losses.loss_factory import LVAELossParameters as LVAELossParameters
from careamics.models.lvae.likelihoods import GaussianLikelihood as GaussianLikelihood, NoiseModelLikelihood as NoiseModelLikelihood, likelihood_factory as likelihood_factory
from careamics.models.lvae.noise_models import GaussianMixtureNoiseModel as GaussianMixtureNoiseModel, MultiChannelNoiseModel as MultiChannelNoiseModel, noise_model_factory as noise_model_factory
from careamics.models.model_factory import model_factory as model_factory
from careamics.transforms import Denormalize as Denormalize, ImageRestorationTTA as ImageRestorationTTA
from careamics.utils.metrics import RunningPSNR as RunningPSNR, scale_invariant_psnr as scale_invariant_psnr
from careamics.utils.torch_utils import get_optimizer as get_optimizer, get_scheduler as get_scheduler
from torch import Tensor as Tensor, nn as nn
from typing import Any, Callable

NoiseModel = GaussianMixtureNoiseModel | MultiChannelNoiseModel

class FCNModule(L.LightningModule):
    model: Incomplete
    loss_func: Incomplete
    optimizer_name: Incomplete
    optimizer_params: Incomplete
    lr_scheduler_name: Incomplete
    lr_scheduler_params: Incomplete
    def __init__(self, algorithm_config: FCNAlgorithmConfig | dict) -> None: ...
    def forward(self, x: Any) -> Any: ...
    def training_step(self, batch: Tensor, batch_idx: Any) -> Any: ...
    def validation_step(self, batch: Tensor, batch_idx: Any) -> None: ...
    def predict_step(self, batch: Tensor, batch_idx: Any) -> Any: ...
    def configure_optimizers(self) -> Any: ...

class VAEModule(L.LightningModule):
    algorithm_config: Incomplete
    model: Incomplete
    noise_model: Incomplete
    noise_model_likelihood: Incomplete
    gaussian_likelihood: Incomplete
    loss_parameters: Incomplete
    loss_func: Incomplete
    optimizer_name: Incomplete
    optimizer_params: Incomplete
    lr_scheduler_name: Incomplete
    lr_scheduler_params: Incomplete
    running_psnr: Incomplete
    def __init__(self, algorithm_config: VAEAlgorithmConfig | dict) -> None: ...
    def forward(self, x: Tensor) -> tuple[Tensor, dict[str, Any]]: ...
    def training_step(self, batch: tuple[Tensor, Tensor], batch_idx: Any) -> dict[str, Tensor] | None: ...
    def validation_step(self, batch: tuple[Tensor, Tensor], batch_idx: Any) -> None: ...
    def on_validation_epoch_end(self) -> None: ...
    def predict_step(self, batch: Tensor, batch_idx: Any) -> Any: ...
    def configure_optimizers(self) -> Any: ...
    def get_reconstructed_tensor(self, model_outputs: tuple[Tensor, dict[str, Any]]) -> Tensor: ...
    def compute_val_psnr(self, model_output: tuple[Tensor, dict[str, Any]], target: Tensor, psnr_func: Callable = ...) -> list[float]: ...
    def reduce_running_psnr(self) -> float | None: ...

def create_careamics_module(algorithm: SupportedAlgorithm | str, loss: SupportedLoss | str, architecture: SupportedArchitecture | str, model_parameters: dict | None = None, optimizer: SupportedOptimizer | str = 'Adam', optimizer_parameters: dict | None = None, lr_scheduler: SupportedScheduler | str = 'ReduceLROnPlateau', lr_scheduler_parameters: dict | None = None) -> FCNModule | VAEModule: ...
