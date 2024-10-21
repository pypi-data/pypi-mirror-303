from .get_func import SupportedWriteType as SupportedWriteType, WriteFunc as WriteFunc, get_write_func as get_write_func
from .tiff import write_tiff as write_tiff

__all__ = ['get_write_func', 'write_tiff', 'WriteFunc', 'SupportedWriteType']
