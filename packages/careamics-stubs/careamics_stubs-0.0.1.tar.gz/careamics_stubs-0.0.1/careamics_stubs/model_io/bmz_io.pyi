import numpy as np
from .bioimage import create_env_text as create_env_text, create_model_description as create_model_description, extract_model_path as extract_model_path, get_unzip_path as get_unzip_path
from bioimageio.spec import ValidationSummary as ValidationSummary
from careamics.config import Configuration as Configuration, load_configuration as load_configuration, save_configuration as save_configuration
from careamics.config.support import SupportedArchitecture as SupportedArchitecture
from careamics.lightning.lightning_module import FCNModule as FCNModule, VAEModule as VAEModule
from pathlib import Path

def export_to_bmz(model: FCNModule | VAEModule, config: Configuration, path_to_archive: Path | str, model_name: str, general_description: str, authors: list[dict], input_array: np.ndarray, output_array: np.ndarray, channel_names: list[str] | None = None, data_description: str | None = None) -> None: ...
def load_from_bmz(path: Path | str) -> tuple[FCNModule | VAEModule, Configuration]: ...
