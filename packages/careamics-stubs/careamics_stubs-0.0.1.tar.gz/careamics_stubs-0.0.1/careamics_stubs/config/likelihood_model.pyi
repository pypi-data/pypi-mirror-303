from _typeshed import Incomplete
from careamics.models.lvae.noise_models import GaussianMixtureNoiseModel as GaussianMixtureNoiseModel, MultiChannelNoiseModel as MultiChannelNoiseModel
from pydantic import BaseModel
from typing import Literal

NoiseModel = GaussianMixtureNoiseModel | MultiChannelNoiseModel
Tensor: Incomplete

class GaussianLikelihoodConfig(BaseModel):
    model_config: Incomplete
    predict_logvar: Literal['pixelwise'] | None
    logvar_lowerbound: float | None

class NMLikelihoodConfig(BaseModel):
    model_config: Incomplete
    data_mean: Tensor
    data_std: Tensor
    noise_model: NoiseModel | None
