from _typeshed import Incomplete
from careamics.config.architectures import CustomModel as CustomModel, UNetModel as UNetModel
from careamics.config.optimizer_models import LrSchedulerModel as LrSchedulerModel, OptimizerModel as OptimizerModel
from pydantic import BaseModel
from typing import Literal
from typing_extensions import Self

class FCNAlgorithmConfig(BaseModel):
    model_config: Incomplete
    algorithm: Literal['n2v', 'care', 'n2n', 'custom']
    loss: Literal['n2v', 'mae', 'mse']
    model: UNetModel | CustomModel
    optimizer: OptimizerModel
    lr_scheduler: LrSchedulerModel
    def algorithm_cross_validation(self) -> Self: ...
    @classmethod
    def get_compatible_algorithms(cls) -> list[str]: ...
