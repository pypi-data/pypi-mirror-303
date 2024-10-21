from .pixel_manipulation import median_manipulate as median_manipulate, uniform_manipulate as uniform_manipulate
from .struct_mask_parameters import StructMaskParameters as StructMaskParameters
from _typeshed import Incomplete
from careamics.config.support import SupportedPixelManipulation as SupportedPixelManipulation, SupportedStructAxis as SupportedStructAxis
from careamics.transforms.transform import Transform as Transform
from numpy.typing import NDArray as NDArray
from typing import Any, Literal

class N2VManipulate(Transform):
    masked_pixel_percentage: Incomplete
    roi_size: Incomplete
    strategy: Incomplete
    remove_center: Incomplete
    struct_mask: Incomplete
    rng: Incomplete
    def __init__(self, roi_size: int = 11, masked_pixel_percentage: float = 0.2, strategy: Literal['uniform', 'median'] = ..., remove_center: bool = True, struct_mask_axis: Literal['horizontal', 'vertical', 'none'] = 'none', struct_mask_span: int = 5, seed: int | None = None) -> None: ...
    def __call__(self, patch: NDArray, *args: Any, **kwargs: Any) -> tuple[NDArray, NDArray, NDArray]: ...
