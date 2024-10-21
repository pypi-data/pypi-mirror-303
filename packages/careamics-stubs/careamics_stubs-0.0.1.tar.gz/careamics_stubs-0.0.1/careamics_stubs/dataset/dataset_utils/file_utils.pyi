from _typeshed import Incomplete
from careamics.config.support import SupportedData as SupportedData
from careamics.utils.logging import get_logger as get_logger
from pathlib import Path

logger: Incomplete

def get_files_size(files: list[Path]) -> float: ...
def list_files(data_path: str | Path, data_type: str | SupportedData, extension_filter: str = '') -> list[Path]: ...
def validate_source_target_files(src_files: list[Path], tar_files: list[Path]) -> None: ...
