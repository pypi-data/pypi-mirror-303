from .types import DataSplitType as DataSplitType, DataType as DataType, TilingMode as TilingMode
from _typeshed import Incomplete
from pydantic import BaseModel
from typing import Any

class DatasetConfig(BaseModel):
    model_config: Incomplete
    data_type: DataType | None
    depth3D: int | None
    datasplit_type: DataSplitType | None
    num_channels: int | None
    ch1_fname: str | None
    ch2_fname: str | None
    ch_input_fname: str | None
    input_is_sum: bool | None
    input_idx: int | None
    target_idx_list: list[int] | None
    start_alpha: Any | None
    end_alpha: Any | None
    image_size: int
    grid_size: int | None
    empty_patch_replacement_enabled: bool | None
    empty_patch_replacement_channel_idx: Any | None
    empty_patch_replacement_probab: Any | None
    empty_patch_max_val_threshold: Any | None
    uncorrelated_channels: bool | None
    uncorrelated_channel_probab: float | None
    poisson_noise_factor: float | None
    synthetic_gaussian_scale: float | None
    input_has_dependant_noise: bool | None
    enable_gaussian_noise: bool | None
    allow_generation: bool
    training_validtarget_fraction: Any
    deterministic_grid: Any
    enable_rotation_aug: bool | None
    max_val: float | None
    overlapping_padding_kwargs: Any
    print_vars: bool | None
    normalized_input: bool
    use_one_mu_std: bool | None
    train_aug_rotate: bool | None
    enable_random_cropping: bool | None
    multiscale_lowres_count: int | None
    tiling_mode: TilingMode | None
    target_separate_normalization: bool | None
    mode_3D: bool | None
    trainig_datausage_fraction: float | None
    validtarget_random_fraction: float | None
    validation_datausage_fraction: float | None
    random_flip_z_3D: bool | None
    padding_kwargs: dict | None
