import numpy as np
from ..utils.logging import get_logger as get_logger
from .dataset_utils import iterate_over_files as iterate_over_files
from .dataset_utils.running_stats import WelfordStatistics as WelfordStatistics
from .patching.patching import Stats as Stats
from .patching.random_patching import extract_patches_random as extract_patches_random
from _typeshed import Incomplete
from careamics.config import DataConfig as DataConfig
from careamics.config.transformations import NormalizeModel as NormalizeModel
from careamics.file_io.read import read_tiff as read_tiff
from careamics.transforms import Compose as Compose
from collections.abc import Generator
from pathlib import Path
from torch.utils.data import IterableDataset
from typing import Callable

logger: Incomplete

class PathIterableDataset(IterableDataset):
    data_config: Incomplete
    data_files: Incomplete
    target_files: Incomplete
    read_source_func: Incomplete
    patch_transform: Incomplete
    def __init__(self, data_config: DataConfig, src_files: list[Path], target_files: list[Path] | None = None, read_source_func: Callable = ...) -> None: ...
    def __iter__(self) -> Generator[tuple[np.ndarray, ...], None, None]: ...
    def get_data_statistics(self) -> tuple[list[float], list[float]]: ...
    def get_number_of_files(self) -> int: ...
    def split_dataset(self, percentage: float = 0.1, minimum_number: int = 5) -> PathIterableDataset: ...
