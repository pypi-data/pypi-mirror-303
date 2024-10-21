from .transform_model import TransformModel as TransformModel
from _typeshed import Incomplete
from typing import Literal
from typing_extensions import Self

class NormalizeModel(TransformModel):
    model_config: Incomplete
    name: Literal['Normalize']
    image_means: list
    image_stds: list
    target_means: list | None
    target_stds: list | None
    def validate_means_stds(self) -> Self: ...
