from ._readme_factory import readme_factory as readme_factory
from bioimageio.spec.model.v0_5 import Author as Author, AxisBase as AxisBase, ModelDescr
from careamics.config import Configuration as Configuration, DataConfig as DataConfig
from pathlib import Path

def create_model_description(config: Configuration, name: str, general_description: str, authors: list[Author], inputs: Path | str, outputs: Path | str, weights_path: Path | str, torch_version: str, careamics_version: str, config_path: Path | str, env_path: Path | str, channel_names: list[str] | None = None, data_description: str | None = None) -> ModelDescr: ...
def extract_model_path(model_desc: ModelDescr) -> tuple[Path, Path]: ...
