from careamics.config import Configuration as Configuration
from careamics.lightning.lightning_module import FCNModule as FCNModule, VAEModule as VAEModule
from careamics.model_io.bmz_io import load_from_bmz as load_from_bmz
from careamics.utils import check_path_exists as check_path_exists
from pathlib import Path

def load_pretrained(path: Path | str) -> tuple[FCNModule | VAEModule, Configuration]: ...
