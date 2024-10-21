import numpy as np
import zarr
from .validate_patch_dimension import validate_patch_dimensions as validate_patch_dimensions
from typing import Generator

def extract_patches_random(arr: np.ndarray, patch_size: list[int] | tuple[int, ...], target: np.ndarray | None = None, seed: int | None = None) -> Generator[tuple[np.ndarray, np.ndarray | None], None, None]: ...
def extract_patches_random_from_chunks(arr: zarr.Array, patch_size: list[int] | tuple[int, ...], chunk_size: list[int] | tuple[int, ...], chunk_limit: int | None = None, seed: int | None = None) -> Generator[np.ndarray, None, None]: ...
