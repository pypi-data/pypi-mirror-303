import numpy as np
from _typeshed import Incomplete
from careamics.config.support import SupportedData as SupportedData
from careamics.utils.logging import get_logger as get_logger
from pathlib import Path

logger: Incomplete

def read_tiff(file_path: Path, *args: list, **kwargs: dict) -> np.ndarray: ...
