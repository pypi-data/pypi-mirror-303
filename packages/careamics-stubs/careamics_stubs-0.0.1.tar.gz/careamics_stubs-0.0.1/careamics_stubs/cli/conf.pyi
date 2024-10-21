import click
import typer
from ..config import Configuration as Configuration, create_care_configuration as create_care_configuration, create_n2n_configuration as create_n2n_configuration, create_n2v_configuration as create_n2v_configuration, save_configuration as save_configuration
from _typeshed import Incomplete
from dataclasses import dataclass
from pathlib import Path
from typing_extensions import Annotated

WORK_DIR: Incomplete
app: Incomplete

@dataclass
class ConfOptions:
    dir: Path
    name: str
    force: bool
    print: bool
    def __init__(self, dir, name, force, print) -> None: ...

def conf_options(ctx: typer.Context, dir: Annotated[Path, None] = ..., name: Annotated[str, None] = 'config', force: Annotated[bool, None] = False, print: Annotated[bool, None] = False): ...
def patch_size_callback(value: tuple[int, int, int]) -> tuple[int, ...]: ...
def care(ctx: typer.Context, experiment_name: Annotated[str, None], axes: Annotated[str, None], patch_size: Annotated[click.Tuple, None], batch_size: Annotated[int, None], num_epochs: Annotated[int, None], data_type: Annotated[click.Choice, None] = 'tiff', use_augmentations: Annotated[bool, None] = True, independent_channels: Annotated[bool, None] = False, loss: Annotated[click.Choice, None] = 'mae', n_channels_in: Annotated[int, None] = 1, n_channels_out: Annotated[int, None] = -1, logger: Annotated[click.Choice, None] = 'none') -> None: ...
def n2n(ctx: typer.Context, experiment_name: Annotated[str, None], axes: Annotated[str, None], patch_size: Annotated[click.Tuple, None], batch_size: Annotated[int, None], num_epochs: Annotated[int, None], data_type: Annotated[click.Choice, None] = 'tiff', use_augmentations: Annotated[bool, None] = True, independent_channels: Annotated[bool, None] = False, loss: Annotated[click.Choice, None] = 'mae', n_channels_in: Annotated[int, None] = 1, n_channels_out: Annotated[int, None] = -1, logger: Annotated[click.Choice, None] = 'none') -> None: ...
def n2v(ctx: typer.Context, experiment_name: Annotated[str, None], axes: Annotated[str, None], patch_size: Annotated[click.Tuple, None], batch_size: Annotated[int, None], num_epochs: Annotated[int, None], data_type: Annotated[click.Choice, None] = 'tiff', use_augmentations: Annotated[bool, None] = True, independent_channels: Annotated[bool, None] = True, use_n2v2: Annotated[bool, None] = False, n_channels: Annotated[int, None] = 1, roi_size: Annotated[int, None] = 11, masked_pixel_percentage: Annotated[float, None] = 0.2, struct_n2v_axis: Annotated[click.Choice, None] = 'none', struct_n2v_span: Annotated[int, None] = 5, logger: Annotated[click.Choice, None] = 'none') -> None: ...
