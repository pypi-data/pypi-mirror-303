import numpy as np
from careamics.config.tile_information import TileInformation as TileInformation
from typing import Any

def collate_tiles(batch: list[tuple[np.ndarray, TileInformation]]) -> Any: ...
