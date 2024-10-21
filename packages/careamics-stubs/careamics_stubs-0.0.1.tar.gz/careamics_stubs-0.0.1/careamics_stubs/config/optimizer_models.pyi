from .support import SupportedOptimizer as SupportedOptimizer
from _typeshed import Incomplete
from careamics.utils.torch_utils import filter_parameters as filter_parameters
from pydantic import BaseModel, ValidationInfo as ValidationInfo
from typing import Literal
from typing_extensions import Self

class OptimizerModel(BaseModel):
    model_config: Incomplete
    name: Literal['Adam', 'SGD', 'Adamax']
    parameters: dict
    @classmethod
    def filter_parameters(cls, user_params: dict, values: ValidationInfo) -> dict: ...
    def sgd_lr_parameter(self) -> Self: ...

class LrSchedulerModel(BaseModel):
    model_config: Incomplete
    name: Literal['ReduceLROnPlateau', 'StepLR']
    parameters: dict
    @classmethod
    def filter_parameters(cls, user_params: dict, values: ValidationInfo) -> dict: ...
