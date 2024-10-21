from .transform_model import TransformModel as TransformModel
from _typeshed import Incomplete
from typing import Literal

class XYRandomRotate90Model(TransformModel):
    model_config: Incomplete
    name: Literal['XYRandomRotate90']
    p: float
    seed: int | None
