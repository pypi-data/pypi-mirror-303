from .architectures import UNetModel as UNetModel
from .configuration_model import Configuration as Configuration
from .data_model import DataConfig as DataConfig
from .fcn_algorithm_model import FCNAlgorithmConfig as FCNAlgorithmConfig
from .support import SupportedArchitecture as SupportedArchitecture, SupportedPixelManipulation as SupportedPixelManipulation, SupportedTransform as SupportedTransform
from .training_model import TrainingConfig as TrainingConfig
from .transformations import N2VManipulateModel as N2VManipulateModel, XYFlipModel as XYFlipModel, XYRandomRotate90Model as XYRandomRotate90Model
from typing import Literal

def create_care_configuration(experiment_name: str, data_type: Literal['array', 'tiff', 'custom'], axes: str, patch_size: list[int], batch_size: int, num_epochs: int, augmentations: list[XYFlipModel | XYRandomRotate90Model] | None = None, independent_channels: bool = True, loss: Literal['mae', 'mse'] = 'mae', n_channels_in: int = 1, n_channels_out: int = -1, logger: Literal['wandb', 'tensorboard', 'none'] = 'none', model_params: dict | None = None, dataloader_params: dict | None = None) -> Configuration: ...
def create_n2n_configuration(experiment_name: str, data_type: Literal['array', 'tiff', 'custom'], axes: str, patch_size: list[int], batch_size: int, num_epochs: int, augmentations: list[XYFlipModel | XYRandomRotate90Model] | None = None, independent_channels: bool = True, loss: Literal['mae', 'mse'] = 'mae', n_channels_in: int = 1, n_channels_out: int = -1, logger: Literal['wandb', 'tensorboard', 'none'] = 'none', model_params: dict | None = None, dataloader_params: dict | None = None) -> Configuration: ...
def create_n2v_configuration(experiment_name: str, data_type: Literal['array', 'tiff', 'custom'], axes: str, patch_size: list[int], batch_size: int, num_epochs: int, augmentations: list[XYFlipModel | XYRandomRotate90Model] | None = None, independent_channels: bool = True, use_n2v2: bool = False, n_channels: int = 1, roi_size: int = 11, masked_pixel_percentage: float = 0.2, struct_n2v_axis: Literal['horizontal', 'vertical', 'none'] = 'none', struct_n2v_span: int = 5, logger: Literal['wandb', 'tensorboard', 'none'] = 'none', model_params: dict | None = None, dataloader_params: dict | None = None) -> Configuration: ...
