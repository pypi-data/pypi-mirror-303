from .validators import check_axes_validity as check_axes_validity, patch_size_ge_than_8_power_of_2 as patch_size_ge_than_8_power_of_2
from _typeshed import Incomplete
from pydantic import BaseModel
from typing import Literal
from typing_extensions import Self

class InferenceConfig(BaseModel):
    model_config: Incomplete
    data_type: Literal['array', 'tiff', 'custom']
    tile_size: list[int] | None
    tile_overlap: list[int] | None
    axes: str
    image_means: list
    image_stds: list
    tta_transforms: bool
    batch_size: int
    @classmethod
    def all_elements_non_zero_even(cls, tile_overlap: list[int] | None) -> list[int] | None: ...
    @classmethod
    def tile_min_8_power_of_2(cls, tile_list: list[int] | None) -> list[int] | None: ...
    @classmethod
    def axes_valid(cls, axes: str) -> str: ...
    def validate_dimensions(self) -> Self: ...
    def std_only_with_mean(self) -> Self: ...
    def set_3D(self, axes: str, tile_size: list[int], tile_overlap: list[int]) -> None: ...
