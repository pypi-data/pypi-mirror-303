from .config import DatasetConfig as DatasetConfig
from .multich_dataset import MultiChDloader as MultiChDloader
from _typeshed import Incomplete
from typing import Callable

class LCMultiChDloader(MultiChDloader):
    multiscale_lowres_count: Incomplete
    def __init__(self, data_config: DatasetConfig, fpath: str, load_data_fn: Callable, val_fraction: Incomplete | None = None, test_fraction: Incomplete | None = None) -> None: ...
    N: Incomplete
    def reduce_data(self, t_list: Incomplete | None = None, h_start: Incomplete | None = None, h_end: Incomplete | None = None, w_start: Incomplete | None = None, w_end: Incomplete | None = None) -> None: ...
    def __getitem__(self, index: int | tuple[int, int]): ...
