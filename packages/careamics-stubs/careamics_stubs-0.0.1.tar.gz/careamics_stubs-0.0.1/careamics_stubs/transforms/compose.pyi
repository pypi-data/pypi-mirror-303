from .n2v_manipulate import N2VManipulate as N2VManipulate
from .normalize import Normalize as Normalize
from .transform import Transform as Transform
from .xy_flip import XYFlip as XYFlip
from .xy_random_rotate90 import XYRandomRotate90 as XYRandomRotate90
from _typeshed import Incomplete
from careamics.config.transformations import TransformModel as TransformModel
from numpy.typing import NDArray

ALL_TRANSFORMS: Incomplete

def get_all_transforms() -> dict[str, type]: ...

class Compose:
    transforms: Incomplete
    def __init__(self, transform_list: list[TransformModel]) -> None: ...
    def __call__(self, patch: NDArray, target: NDArray | None = None) -> tuple[NDArray, ...]: ...
    def transform_with_additional_arrays(self, patch: NDArray, target: NDArray | None = None, **additional_arrays: NDArray) -> tuple[NDArray, NDArray | None, dict[str, NDArray]]: ...
