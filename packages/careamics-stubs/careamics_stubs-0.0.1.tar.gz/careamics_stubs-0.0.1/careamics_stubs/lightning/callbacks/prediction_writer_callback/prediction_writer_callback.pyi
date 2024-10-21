from .write_strategy import WriteStrategy as WriteStrategy
from .write_strategy_factory import create_write_strategy as create_write_strategy
from _typeshed import Incomplete
from careamics.dataset import IterablePredDataset as IterablePredDataset, IterableTiledPredDataset as IterableTiledPredDataset
from careamics.file_io import SupportedWriteType as SupportedWriteType, WriteFunc as WriteFunc
from careamics.utils import get_logger as get_logger
from pathlib import Path
from pytorch_lightning import LightningModule as LightningModule, Trainer as Trainer
from pytorch_lightning.callbacks import BasePredictionWriter
from torch.utils.data import DataLoader as DataLoader
from typing import Any, Sequence

logger: Incomplete
ValidPredDatasets = IterablePredDataset | IterableTiledPredDataset

class PredictionWriterCallback(BasePredictionWriter):
    writing_predictions: bool
    write_strategy: Incomplete
    dirpath: Incomplete
    def __init__(self, write_strategy: WriteStrategy, dirpath: Path | str = 'predictions') -> None: ...
    @classmethod
    def from_write_func_params(cls, write_type: SupportedWriteType, tiled: bool, write_func: WriteFunc | None = None, write_extension: str | None = None, write_func_kwargs: dict[str, Any] | None = None, dirpath: Path | str = 'predictions') -> PredictionWriterCallback: ...
    def setup(self, trainer: Trainer, pl_module: LightningModule, stage: str) -> None: ...
    def write_on_batch_end(self, trainer: Trainer, pl_module: LightningModule, prediction: Any, batch_indices: Sequence[int] | None, batch: Any, batch_idx: int, dataloader_idx: int) -> None: ...
