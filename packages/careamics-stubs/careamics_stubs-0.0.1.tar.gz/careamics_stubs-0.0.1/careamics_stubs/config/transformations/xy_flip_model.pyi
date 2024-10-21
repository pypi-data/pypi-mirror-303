from .transform_model import TransformModel as TransformModel
from _typeshed import Incomplete
from typing import Literal

class XYFlipModel(TransformModel):
    model_config: Incomplete
    name: Literal['XYFlip']
    flip_x: bool
    flip_y: bool
    p: float
    seed: int | None
