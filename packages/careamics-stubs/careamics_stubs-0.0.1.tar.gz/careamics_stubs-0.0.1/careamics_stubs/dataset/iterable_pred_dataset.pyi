from ..config import InferenceConfig as InferenceConfig
from ..config.transformations import NormalizeModel as NormalizeModel
from .dataset_utils import iterate_over_files as iterate_over_files
from _typeshed import Incomplete
from careamics.file_io.read import read_tiff as read_tiff
from careamics.transforms import Compose as Compose
from numpy.typing import NDArray as NDArray
from pathlib import Path
from torch.utils.data import IterableDataset
from typing import Any, Callable, Generator

class IterablePredDataset(IterableDataset):
    prediction_config: Incomplete
    data_files: Incomplete
    axes: Incomplete
    read_source_func: Incomplete
    image_means: Incomplete
    image_stds: Incomplete
    patch_transform: Incomplete
    def __init__(self, prediction_config: InferenceConfig, src_files: list[Path], read_source_func: Callable = ..., **kwargs: Any) -> None: ...
    def __iter__(self) -> Generator[NDArray, None, None]: ...
