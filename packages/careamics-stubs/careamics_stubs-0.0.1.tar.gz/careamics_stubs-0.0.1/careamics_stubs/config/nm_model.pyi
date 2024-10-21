import numpy as np
from _typeshed import Incomplete
from pathlib import Path
from pydantic import BaseModel
from typing import Literal
from typing_extensions import Self

Array: Incomplete

class GaussianMixtureNMConfig(BaseModel):
    model_config: Incomplete
    model_type: Literal['GaussianMixtureNoiseModel']
    path: Path | str | None
    signal: str | Path | np.ndarray | None
    observation: str | Path | np.ndarray | None
    weight: Array | None
    n_gaussian: int
    n_coeff: int
    min_signal: float
    max_signal: float
    min_sigma: float
    tol: float
    def validate_path_to_pretrained_vs_training_data(self) -> Self: ...

class MultiChannelNMConfig(BaseModel):
    model_config: Incomplete
    noise_models: list[GaussianMixtureNMConfig]
