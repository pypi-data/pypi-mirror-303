from _typeshed import Incomplete
from careamics.transforms.transform import Transform as Transform
from numpy.typing import NDArray as NDArray

class XYRandomRotate90(Transform):
    p: Incomplete
    rng: Incomplete
    def __init__(self, p: float = 0.5, seed: int | None = None) -> None: ...
    def __call__(self, patch: NDArray, target: NDArray | None = None, **additional_arrays: NDArray) -> tuple[NDArray, NDArray | None, dict[str, NDArray]]: ...
