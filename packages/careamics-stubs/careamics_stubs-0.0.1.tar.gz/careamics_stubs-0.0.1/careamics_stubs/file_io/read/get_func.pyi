from .tiff import read_tiff as read_tiff
from careamics.config.support import SupportedData as SupportedData
from numpy.typing import NDArray as NDArray
from pathlib import Path
from typing import Callable, Protocol

class ReadFunc(Protocol):
    def __call__(self, file_path: Path, *args, **kwargs) -> NDArray: ...

READ_FUNCS: dict[SupportedData, ReadFunc]

def get_read_func(data_type: str | SupportedData) -> Callable: ...
