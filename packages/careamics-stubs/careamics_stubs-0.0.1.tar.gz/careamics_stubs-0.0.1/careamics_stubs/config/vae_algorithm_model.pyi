from .architectures import CustomModel as CustomModel, LVAEModel as LVAEModel
from .likelihood_model import GaussianLikelihoodConfig as GaussianLikelihoodConfig, NMLikelihoodConfig as NMLikelihoodConfig
from .nm_model import MultiChannelNMConfig as MultiChannelNMConfig
from .optimizer_models import LrSchedulerModel as LrSchedulerModel, OptimizerModel as OptimizerModel
from _typeshed import Incomplete
from careamics.config.support import SupportedAlgorithm as SupportedAlgorithm, SupportedLoss as SupportedLoss
from pydantic import BaseModel
from typing import Literal
from typing_extensions import Self

class VAEAlgorithmConfig(BaseModel):
    model_config: Incomplete
    algorithm: Literal['musplit', 'denoisplit']
    loss: Literal['musplit', 'denoisplit', 'denoisplit_musplit']
    model: LVAEModel | CustomModel
    noise_model: MultiChannelNMConfig | None
    noise_model_likelihood_model: NMLikelihoodConfig | None
    gaussian_likelihood_model: GaussianLikelihoodConfig | None
    optimizer: OptimizerModel
    lr_scheduler: LrSchedulerModel
    def algorithm_cross_validation(self) -> Self: ...
    def output_channels_validation(self) -> Self: ...
    def predict_logvar_validation(self) -> Self: ...
