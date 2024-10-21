from _typeshed import Incomplete
from datetime import timedelta
from pydantic import BaseModel
from typing import Literal

class CheckpointModel(BaseModel):
    model_config: Incomplete
    monitor: Literal['val_loss']
    verbose: bool
    save_weights_only: bool
    save_last: Literal[True, False, 'link'] | None
    save_top_k: int
    mode: Literal['min', 'max']
    auto_insert_metric_name: bool
    every_n_train_steps: int | None
    train_time_interval: timedelta | None
    every_n_epochs: int | None

class EarlyStoppingModel(BaseModel):
    model_config: Incomplete
    monitor: Literal['val_loss']
    min_delta: float
    patience: int
    verbose: bool
    mode: Literal['min', 'max', 'auto']
    check_finite: bool
    stopping_threshold: float | None
    divergence_threshold: float | None
    check_on_train_epoch_end: bool | None
    log_rank_zero_only: bool
