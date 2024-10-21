from _typeshed import Incomplete
from careamics.transforms.transform import Transform as Transform
from numpy.typing import NDArray as NDArray

class XYFlip(Transform):
    p: Incomplete
    axis_indices: Incomplete
    rng: Incomplete
    def __init__(self, flip_x: bool = True, flip_y: bool = True, p: float = 0.5, seed: int | None = None) -> None: ...
    def __call__(self, patch: NDArray, target: NDArray | None = None, **additional_arrays: NDArray) -> tuple[NDArray, NDArray | None, dict[str, NDArray]]: ...
