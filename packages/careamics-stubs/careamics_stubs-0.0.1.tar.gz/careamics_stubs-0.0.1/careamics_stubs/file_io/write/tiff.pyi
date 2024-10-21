from careamics.config.support import SupportedData as SupportedData
from numpy.typing import NDArray as NDArray
from pathlib import Path

def write_tiff(file_path: Path, img: NDArray, *args, **kwargs) -> None: ...
