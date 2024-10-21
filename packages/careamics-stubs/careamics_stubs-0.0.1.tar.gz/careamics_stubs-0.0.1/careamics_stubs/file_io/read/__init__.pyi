from .get_func import ReadFunc as ReadFunc, get_read_func as get_read_func
from .tiff import read_tiff as read_tiff
from .zarr import read_zarr as read_zarr

__all__ = ['get_read_func', 'read_tiff', 'read_zarr', 'ReadFunc']
