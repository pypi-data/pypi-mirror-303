from .file_path_utils import create_write_file_path as create_write_file_path, get_sample_file_path as get_sample_file_path
from _typeshed import Incomplete
from careamics.config.tile_information import TileInformation as TileInformation
from careamics.dataset import IterablePredDataset as IterablePredDataset, IterableTiledPredDataset as IterableTiledPredDataset
from careamics.file_io import WriteFunc as WriteFunc
from careamics.prediction_utils import stitch_prediction_single as stitch_prediction_single
from numpy.typing import NDArray as NDArray
from pathlib import Path
from pytorch_lightning import LightningModule as LightningModule, Trainer as Trainer
from torch.utils.data import DataLoader as DataLoader
from typing import Any, Protocol, Sequence

class WriteStrategy(Protocol):
    def write_batch(self, trainer: Trainer, pl_module: LightningModule, prediction: Any, batch_indices: Sequence[int] | None, batch: Any, batch_idx: int, dataloader_idx: int, dirpath: Path) -> None: ...

class CacheTiles(WriteStrategy):
    write_func: Incomplete
    write_extension: Incomplete
    write_func_kwargs: Incomplete
    tile_cache: Incomplete
    tile_info_cache: Incomplete
    def __init__(self, write_func: WriteFunc, write_extension: str, write_func_kwargs: dict[str, Any]) -> None: ...
    @property
    def last_tiles(self) -> list[bool]: ...
    def write_batch(self, trainer: Trainer, pl_module: LightningModule, prediction: tuple[NDArray, list[TileInformation]], batch_indices: Sequence[int] | None, batch: tuple[NDArray, list[TileInformation]], batch_idx: int, dataloader_idx: int, dirpath: Path) -> None: ...

class WriteTilesZarr(WriteStrategy):
    def write_batch(self, trainer: Trainer, pl_module: LightningModule, prediction: Any, batch_indices: Sequence[int] | None, batch: Any, batch_idx: int, dataloader_idx: int, dirpath: Path) -> None: ...

class WriteImage(WriteStrategy):
    write_func: Incomplete
    write_extension: Incomplete
    write_func_kwargs: Incomplete
    def __init__(self, write_func: WriteFunc, write_extension: str, write_func_kwargs: dict[str, Any]) -> None: ...
    def write_batch(self, trainer: Trainer, pl_module: LightningModule, prediction: NDArray, batch_indices: Sequence[int] | None, batch: NDArray, batch_idx: int, dataloader_idx: int, dirpath: Path) -> None: ...
