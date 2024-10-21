import pytorch_lightning as L
from _typeshed import Incomplete
from careamics.config import InferenceConfig as InferenceConfig
from careamics.config.support import SupportedData as SupportedData
from careamics.dataset import InMemoryPredDataset as InMemoryPredDataset, InMemoryTiledPredDataset as InMemoryTiledPredDataset, IterablePredDataset as IterablePredDataset, IterableTiledPredDataset as IterableTiledPredDataset
from careamics.dataset.dataset_utils import list_files as list_files
from careamics.dataset.tiling.collate_tiles import collate_tiles as collate_tiles
from careamics.file_io.read import get_read_func as get_read_func
from careamics.utils import get_logger as get_logger
from numpy.typing import NDArray as NDArray
from pathlib import Path
from torch.utils.data import DataLoader
from typing import Callable, Literal

PredictDatasetType = InMemoryPredDataset | InMemoryTiledPredDataset | IterablePredDataset | IterableTiledPredDataset
logger: Incomplete

class PredictDataModule(L.LightningDataModule):
    prediction_config: Incomplete
    data_type: Incomplete
    batch_size: Incomplete
    dataloader_params: Incomplete
    pred_data: Incomplete
    tile_size: Incomplete
    tile_overlap: Incomplete
    tiled: Incomplete
    read_source_func: Incomplete
    extension_filter: Incomplete
    def __init__(self, pred_config: InferenceConfig, pred_data: Path | str | NDArray, read_source_func: Callable | None = None, extension_filter: str = '', dataloader_params: dict | None = None) -> None: ...
    pred_files: Incomplete
    def prepare_data(self) -> None: ...
    predict_dataset: Incomplete
    def setup(self, stage: str | None = None) -> None: ...
    def predict_dataloader(self) -> DataLoader: ...

def create_predict_datamodule(pred_data: str | Path | NDArray, data_type: Literal['array', 'tiff', 'custom'] | SupportedData, axes: str, image_means: list[float], image_stds: list[float], tile_size: tuple[int, ...] | None = None, tile_overlap: tuple[int, ...] | None = None, batch_size: int = 1, tta_transforms: bool = True, read_source_func: Callable | None = None, extension_filter: str = '', dataloader_params: dict | None = None) -> PredictDataModule: ...
