import numpy as np
from .validate_patch_dimension import validate_patch_dimensions as validate_patch_dimensions

def extract_patches_sequential(arr: np.ndarray, patch_size: list[int] | tuple[int, ...], target: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray | None]: ...
