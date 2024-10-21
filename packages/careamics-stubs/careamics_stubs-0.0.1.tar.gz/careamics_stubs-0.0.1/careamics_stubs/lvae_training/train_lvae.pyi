from careamics.lvae_training.train_utils import *
import torch
from _typeshed import Incomplete
from careamics.lvae_training.dataset.data_modules import LCMultiChDloader as LCMultiChDloader, MultiChDloader as MultiChDloader
from careamics.lvae_training.dataset.utils.data_utils import DataSplitType as DataSplitType
from careamics.lvae_training.lightning_module import LadderVAELight as LadderVAELight
from pytorch_lightning.callbacks import ModelCheckpoint
from pytorch_lightning.loggers import WandbLogger
from torch.utils.data import DataLoader

FLAGS: Incomplete

def create_dataset(config, datadir, eval_datasplit_type=..., raw_data_dict: Incomplete | None = None, skip_train_dataset: bool = False, kwargs_dict: Incomplete | None = None): ...
def create_model_and_train(config: ml_collections.ConfigDict, data_mean: dict[str, torch.Tensor], data_std: dict[str, torch.Tensor], logger: WandbLogger, checkpoint_callback: ModelCheckpoint, train_loader: DataLoader, val_loader: DataLoader): ...
def train_network(train_loader: DataLoader, val_loader: DataLoader, data_mean: dict[str, torch.Tensor], data_std: dict[str, torch.Tensor], config: ml_collections.ConfigDict, model_name: str, logdir: str): ...
def main(argv) -> None: ...
