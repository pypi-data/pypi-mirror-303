import numpy as np
from careamics.config.tile_information import TileInformation as TileInformation
from typing import Generator

def extract_tiles(arr: np.ndarray, tile_size: list[int] | tuple[int, ...], overlaps: list[int] | tuple[int, ...]) -> Generator[tuple[np.ndarray, TileInformation], None, None]: ...
