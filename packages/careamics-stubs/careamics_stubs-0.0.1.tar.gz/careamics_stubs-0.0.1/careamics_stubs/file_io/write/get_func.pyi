from .tiff import write_tiff as write_tiff
from _typeshed import Incomplete
from careamics.config.support import SupportedData as SupportedData
from numpy.typing import NDArray as NDArray
from pathlib import Path
from typing import Protocol

SupportedWriteType: Incomplete

class WriteFunc(Protocol):
    def __call__(self, file_path: Path, img: NDArray, *args, **kwargs) -> None: ...

WRITE_FUNCS: dict[SupportedData, WriteFunc]

def get_write_func(data_type: SupportedWriteType) -> WriteFunc: ...
