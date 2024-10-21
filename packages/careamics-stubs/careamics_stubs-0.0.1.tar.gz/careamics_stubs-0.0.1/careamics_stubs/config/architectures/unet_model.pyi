from .architecture_model import ArchitectureModel as ArchitectureModel
from _typeshed import Incomplete
from typing import Literal

class UNetModel(ArchitectureModel):
    model_config: Incomplete
    architecture: Literal['UNet']
    conv_dims: Literal[2, 3]
    num_classes: int
    in_channels: int
    depth: int
    num_channels_init: int
    final_activation: Literal['None', 'Sigmoid', 'Softmax', 'Tanh', 'ReLU', 'LeakyReLU']
    n2v2: bool
    independent_channels: bool
    @classmethod
    def validate_num_channels_init(cls, num_channels_init: int) -> int: ...
    def set_3D(self, is_3D: bool) -> None: ...
    def is_3D(self) -> bool: ...
