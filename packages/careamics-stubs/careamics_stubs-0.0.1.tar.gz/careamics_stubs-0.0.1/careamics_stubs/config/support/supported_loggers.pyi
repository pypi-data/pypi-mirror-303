from careamics.utils import BaseEnum as BaseEnum

class SupportedLogger(str, BaseEnum):
    WANDB = 'wandb'
    TENSORBOARD = 'tensorboard'
