from careamics.config import Configuration as Configuration
from careamics.utils import cwd as cwd, get_careamics_home as get_careamics_home
from pathlib import Path

def readme_factory(config: Configuration, careamics_version: str, data_description: str | None = None) -> Path: ...
