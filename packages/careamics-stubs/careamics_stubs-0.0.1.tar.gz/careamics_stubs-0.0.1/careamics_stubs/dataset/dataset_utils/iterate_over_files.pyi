from .dataset_utils import reshape_array as reshape_array
from _typeshed import Incomplete
from careamics.config import DataConfig as DataConfig, InferenceConfig as InferenceConfig
from careamics.file_io.read import read_tiff as read_tiff
from careamics.utils.logging import get_logger as get_logger
from numpy.typing import NDArray as NDArray
from pathlib import Path
from typing import Callable, Generator

logger: Incomplete

def iterate_over_files(data_config: DataConfig | InferenceConfig, data_files: list[Path], target_files: list[Path] | None = None, read_source_func: Callable = ...) -> Generator[tuple[NDArray, NDArray | None], None, None]: ...
