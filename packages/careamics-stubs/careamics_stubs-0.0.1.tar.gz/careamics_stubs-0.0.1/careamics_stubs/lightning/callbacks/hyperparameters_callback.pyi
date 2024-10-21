from _typeshed import Incomplete
from careamics.config import Configuration as Configuration
from pytorch_lightning import LightningModule as LightningModule, Trainer as Trainer
from pytorch_lightning.callbacks import Callback

class HyperParametersCallback(Callback):
    config: Incomplete
    def __init__(self, config: Configuration) -> None: ...
    def on_train_start(self, trainer: Trainer, pl_module: LightningModule) -> None: ...
