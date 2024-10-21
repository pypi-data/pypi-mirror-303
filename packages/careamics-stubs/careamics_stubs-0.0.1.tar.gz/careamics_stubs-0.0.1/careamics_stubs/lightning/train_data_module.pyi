import pytorch_lightning as L
from _typeshed import Incomplete
from careamics.config import DataConfig as DataConfig
from careamics.config.support import SupportedData as SupportedData
from careamics.config.transformations import TransformModel as TransformModel
from careamics.dataset.dataset_utils import get_files_size as get_files_size, list_files as list_files, validate_source_target_files as validate_source_target_files
from careamics.dataset.in_memory_dataset import InMemoryDataset as InMemoryDataset
from careamics.dataset.iterable_dataset import PathIterableDataset as PathIterableDataset
from careamics.file_io.read import get_read_func as get_read_func
from careamics.utils import get_logger as get_logger, get_ram_size as get_ram_size
from numpy.typing import NDArray as NDArray
from pathlib import Path
from typing import Any, Callable, Literal

DatasetType = InMemoryDataset | PathIterableDataset
logger: Incomplete

class TrainDataModule(L.LightningDataModule):
    data_config: Incomplete
    data_type: Incomplete
    batch_size: Incomplete
    use_in_memory: Incomplete
    train_data: Incomplete
    val_data: Incomplete
    train_data_target: Incomplete
    val_data_target: Incomplete
    val_percentage: Incomplete
    val_minimum_split: Incomplete
    read_source_func: Incomplete
    extension_filter: Incomplete
    dataloader_params: Incomplete
    def __init__(self, data_config: DataConfig, train_data: Path | str | NDArray, val_data: Path | str | NDArray | None = None, train_data_target: Path | str | NDArray | None = None, val_data_target: Path | str | NDArray | None = None, read_source_func: Callable | None = None, extension_filter: str = '', val_percentage: float = 0.1, val_minimum_split: int = 5, use_in_memory: bool = True) -> None: ...
    train_files: Incomplete
    train_files_size: Incomplete
    val_files: Incomplete
    train_target_files: Incomplete
    val_target_files: Incomplete
    def prepare_data(self) -> None: ...
    train_dataset: Incomplete
    val_dataset: Incomplete
    def setup(self, *args: Any, **kwargs: Any) -> None: ...
    def get_data_statistics(self) -> tuple[list[float], list[float]]: ...
    def train_dataloader(self) -> Any: ...
    def val_dataloader(self) -> Any: ...

def create_train_datamodule(train_data: str | Path | NDArray, data_type: Literal['array', 'tiff', 'custom'] | SupportedData, patch_size: list[int], axes: str, batch_size: int, val_data: str | Path | NDArray | None = None, transforms: list[TransformModel] | None = None, train_target_data: str | Path | NDArray | None = None, val_target_data: str | Path | NDArray | None = None, read_source_func: Callable | None = None, extension_filter: str = '', val_percentage: float = 0.1, val_minimum_patches: int = 5, dataloader_params: dict | None = None, use_in_memory: bool = True, use_n2v2: bool = False, struct_n2v_axis: Literal['horizontal', 'vertical', 'none'] = 'none', struct_n2v_span: int = 5) -> TrainDataModule: ...
