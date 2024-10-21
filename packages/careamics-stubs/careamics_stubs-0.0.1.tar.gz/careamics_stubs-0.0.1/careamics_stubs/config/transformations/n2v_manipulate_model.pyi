from .transform_model import TransformModel as TransformModel
from _typeshed import Incomplete
from typing import Literal

class N2VManipulateModel(TransformModel):
    model_config: Incomplete
    name: Literal['N2VManipulate']
    roi_size: int
    masked_pixel_percentage: float
    strategy: Literal['uniform', 'median']
    struct_mask_axis: Literal['horizontal', 'vertical', 'none']
    struct_mask_span: int
    @classmethod
    def odd_value(cls, v: int) -> int: ...
