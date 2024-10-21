from .callback_model import CheckpointModel as CheckpointModel, EarlyStoppingModel as EarlyStoppingModel
from _typeshed import Incomplete
from pydantic import BaseModel
from typing import Literal

class TrainingConfig(BaseModel):
    model_config: Incomplete
    num_epochs: int
    precision: Literal['64', '32', '16-mixed', 'bf16-mixed']
    max_steps: int
    check_val_every_n_epoch: int
    enable_progress_bar: bool
    accumulate_grad_batches: int
    gradient_clip_val: int | float | None
    gradient_clip_algorithm: Literal['value', 'norm']
    logger: Literal['wandb', 'tensorboard'] | None
    checkpoint_callback: CheckpointModel
    early_stopping_callback: EarlyStoppingModel | None
    def has_logger(self) -> bool: ...
    @classmethod
    def validate_max_steps(cls, max_steps: int) -> int: ...
