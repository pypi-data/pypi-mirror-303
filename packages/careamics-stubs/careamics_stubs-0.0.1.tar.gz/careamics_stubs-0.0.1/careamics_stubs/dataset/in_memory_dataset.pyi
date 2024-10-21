import numpy as np
from ..config import DataConfig as DataConfig
from ..config.transformations import NormalizeModel as NormalizeModel
from ..utils.logging import get_logger as get_logger
from .patching.patching import PatchedOutput as PatchedOutput, Stats as Stats, prepare_patches_supervised as prepare_patches_supervised, prepare_patches_supervised_array as prepare_patches_supervised_array, prepare_patches_unsupervised as prepare_patches_unsupervised, prepare_patches_unsupervised_array as prepare_patches_unsupervised_array
from _typeshed import Incomplete
from careamics.file_io.read import read_tiff as read_tiff
from careamics.transforms import Compose as Compose
from pathlib import Path
from torch.utils.data import Dataset
from typing import Any, Callable

logger: Incomplete

class InMemoryDataset(Dataset):
    data_config: Incomplete
    inputs: Incomplete
    input_targets: Incomplete
    axes: Incomplete
    patch_size: Incomplete
    read_source_func: Incomplete
    data: Incomplete
    data_targets: Incomplete
    image_stats: Incomplete
    target_stats: Incomplete
    patch_transform: Incomplete
    def __init__(self, data_config: DataConfig, inputs: np.ndarray | list[Path], input_target: np.ndarray | list[Path] | None = None, read_source_func: Callable = ..., **kwargs: Any) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> tuple[np.ndarray, ...]: ...
    def get_data_statistics(self) -> tuple[list[float], list[float]]: ...
    def split_dataset(self, percentage: float = 0.1, minimum_patches: int = 1) -> InMemoryDataset: ...
