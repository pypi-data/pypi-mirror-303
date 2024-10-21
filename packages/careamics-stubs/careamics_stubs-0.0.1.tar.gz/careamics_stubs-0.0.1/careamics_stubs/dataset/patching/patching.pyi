from ...utils.logging import get_logger as get_logger
from ..dataset_utils import reshape_array as reshape_array
from ..dataset_utils.running_stats import compute_normalization_stats as compute_normalization_stats
from .sequential_patching import extract_patches_sequential as extract_patches_sequential
from _typeshed import Incomplete
from dataclasses import dataclass
from numpy.typing import NDArray as NDArray
from pathlib import Path
from typing import Callable

logger: Incomplete

@dataclass
class Stats:
    means: NDArray | tuple | list | None
    stds: NDArray | tuple | list | None
    def get_statistics(self) -> tuple[list[float], list[float]]: ...
    def __init__(self, means, stds) -> None: ...

@dataclass
class PatchedOutput:
    patches: NDArray
    targets: NDArray | None
    image_stats: Stats
    target_stats: Stats
    def __init__(self, patches, targets, image_stats, target_stats) -> None: ...

def prepare_patches_supervised(train_files: list[Path], target_files: list[Path], axes: str, patch_size: list[int] | tuple[int, ...], read_source_func: Callable) -> PatchedOutput: ...
def prepare_patches_unsupervised(train_files: list[Path], axes: str, patch_size: list[int] | tuple[int], read_source_func: Callable) -> PatchedOutput: ...
def prepare_patches_supervised_array(data: NDArray, axes: str, data_target: NDArray, patch_size: list[int] | tuple[int]) -> PatchedOutput: ...
def prepare_patches_unsupervised_array(data: NDArray, axes: str, patch_size: list[int] | tuple[int]) -> PatchedOutput: ...
