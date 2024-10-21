import logging
from _typeshed import Incomplete
from pathlib import Path
from typing import Generator

LOGGERS: dict

def get_logger(name: str, log_level: int = ..., log_path: str | Path | None = None) -> logging.Logger: ...

class ProgressBar:
    max_value: Incomplete
    width: int
    always_stateful: Incomplete
    stateful_metrics: Incomplete
    spin: Incomplete
    message: str
    def __init__(self, max_value: int | None = None, epoch: int | None = None, num_epochs: int | None = None, stateful_metrics: list | None = None, always_stateful: bool = False, mode: str = 'train') -> None: ...
    def update(self, current_step: int, batch_size: int = 1, values: list | None = None) -> None: ...
    def add(self, n: int, values: list | None = None) -> None: ...
    def spinning_cursor(self) -> Generator: ...
