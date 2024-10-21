from _typeshed import Incomplete
from careamics.config import Configuration as Configuration, FCNAlgorithmConfig as FCNAlgorithmConfig, load_configuration as load_configuration
from careamics.config.support import SupportedAlgorithm as SupportedAlgorithm, SupportedArchitecture as SupportedArchitecture, SupportedData as SupportedData, SupportedLogger as SupportedLogger
from careamics.dataset.dataset_utils import list_files as list_files, reshape_array as reshape_array
from careamics.file_io import WriteFunc as WriteFunc, get_write_func as get_write_func
from careamics.lightning import FCNModule as FCNModule, HyperParametersCallback as HyperParametersCallback, PredictDataModule as PredictDataModule, ProgressBarCallback as ProgressBarCallback, TrainDataModule as TrainDataModule, create_predict_datamodule as create_predict_datamodule
from careamics.model_io import export_to_bmz as export_to_bmz, load_pretrained as load_pretrained
from careamics.prediction_utils import convert_outputs as convert_outputs
from careamics.utils import check_path_exists as check_path_exists, get_logger as get_logger
from numpy.typing import NDArray as NDArray
from pathlib import Path
from pytorch_lightning.callbacks import Callback as Callback
from pytorch_lightning.loggers import TensorBoardLogger, WandbLogger
from typing import Any, Callable, Literal, overload

logger: Incomplete
LOGGER_TYPES = TensorBoardLogger | WandbLogger | None

class CAREamist:
    @overload
    def __init__(self, source: Path | str, work_dir: Path | str | None = None, callbacks: list[Callback] | None = None) -> None: ...
    @overload
    def __init__(self, source: Configuration, work_dir: Path | str | None = None, callbacks: list[Callback] | None = None) -> None: ...
    def stop_training(self) -> None: ...
    def train(self, *, datamodule: TrainDataModule | None = None, train_source: Path | str | NDArray | None = None, val_source: Path | str | NDArray | None = None, train_target: Path | str | NDArray | None = None, val_target: Path | str | NDArray | None = None, use_in_memory: bool = True, val_percentage: float = 0.1, val_minimum_split: int = 1) -> None: ...
    @overload
    def predict(self, source: PredictDataModule) -> list[NDArray] | NDArray: ...
    @overload
    def predict(self, source: Path | str, *, batch_size: int = 1, tile_size: tuple[int, ...] | None = None, tile_overlap: tuple[int, ...] | None = (48, 48), axes: str | None = None, data_type: Literal['tiff', 'custom'] | None = None, tta_transforms: bool = False, dataloader_params: dict | None = None, read_source_func: Callable | None = None, extension_filter: str = '') -> list[NDArray] | NDArray: ...
    @overload
    def predict(self, source: NDArray, *, batch_size: int = 1, tile_size: tuple[int, ...] | None = None, tile_overlap: tuple[int, ...] | None = (48, 48), axes: str | None = None, data_type: Literal['array'] | None = None, tta_transforms: bool = False, dataloader_params: dict | None = None) -> list[NDArray] | NDArray: ...
    def predict_to_disk(self, source: PredictDataModule | Path | str, *, batch_size: int = 1, tile_size: tuple[int, ...] | None = None, tile_overlap: tuple[int, ...] | None = (48, 48), axes: str | None = None, data_type: Literal['tiff', 'custom'] | None = None, tta_transforms: bool = False, dataloader_params: dict | None = None, read_source_func: Callable | None = None, extension_filter: str = '', write_type: Literal['tiff', 'custom'] = 'tiff', write_extension: str | None = None, write_func: WriteFunc | None = None, write_func_kwargs: dict[str, Any] | None = None, prediction_dir: Path | str = 'predictions', **kwargs) -> None: ...
    def export_to_bmz(self, path_to_archive: Path | str, friendly_model_name: str, input_array: NDArray, authors: list[dict], general_description: str = '', channel_names: list[str] | None = None, data_description: str | None = None) -> None: ...
