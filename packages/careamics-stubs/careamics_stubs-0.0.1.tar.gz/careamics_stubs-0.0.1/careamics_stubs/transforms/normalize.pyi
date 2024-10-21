import numpy as np
from _typeshed import Incomplete
from careamics.transforms.transform import Transform as Transform
from numpy.typing import NDArray as NDArray

class Normalize(Transform):
    image_means: Incomplete
    image_stds: Incomplete
    target_means: Incomplete
    target_stds: Incomplete
    eps: float
    def __init__(self, image_means: list[float], image_stds: list[float], target_means: list[float] | None = None, target_stds: list[float] | None = None) -> None: ...
    def __call__(self, patch: np.ndarray, target: NDArray | None = None, **additional_arrays: NDArray) -> tuple[NDArray, NDArray | None, dict[str, NDArray]]: ...

class Denormalize:
    image_means: Incomplete
    image_stds: Incomplete
    eps: float
    def __init__(self, image_means: list[float], image_stds: list[float]) -> None: ...
    def __call__(self, patch: NDArray) -> NDArray: ...
