from . import conf as conf
from ..careamist import CAREamist as CAREamist
from _typeshed import Incomplete
from pathlib import Path
from typing_extensions import Annotated

app: Incomplete

def train(source: Annotated[Path, None], train_source: Annotated[Path, None], train_target: Annotated[Path | None, None] = None, val_source: Annotated[Path | None, None] = None, val_target: Annotated[Path | None, None] = None, use_in_memory: Annotated[bool, None] = True, val_percentage: Annotated[float, None] = 0.1, val_minimum_split: Annotated[int, None] = 1, work_dir: Annotated[Path | None, None] = None): ...
def predict() -> None: ...
def run() -> None: ...
