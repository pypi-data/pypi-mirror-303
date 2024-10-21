from .architecture_model import ArchitectureModel as ArchitectureModel
from _typeshed import Incomplete
from typing import Literal
from typing_extensions import Self

class LVAEModel(ArchitectureModel):
    model_config: Incomplete
    architecture: Literal['LVAE']
    input_shape: list[int]
    encoder_conv_strides: list
    decoder_conv_strides: list
    multiscale_count: int
    z_dims: list
    output_channels: int
    encoder_n_filters: int
    decoder_n_filters: int
    encoder_dropout: float
    decoder_dropout: float
    nonlinearity: Literal['None', 'Sigmoid', 'Softmax', 'Tanh', 'ReLU', 'LeakyReLU', 'ELU']
    predict_logvar: Literal[None, 'pixelwise']
    analytical_kl: bool
    def validate_conv_strides(self) -> Self: ...
    @classmethod
    def validate_input_shape(cls, input_shape: list) -> list: ...
    @classmethod
    def validate_encoder_even(cls, encoder_n_filters: int) -> int: ...
    @classmethod
    def validate_decoder_even(cls, decoder_n_filters: int) -> int: ...
    def validate_z_dims(cls, z_dims: tuple) -> tuple: ...
    def validate_multiscale_count(self) -> Self: ...
    conv_dims: int
    def set_3D(self, is_3D: bool) -> None: ...
    def is_3D(self) -> bool: ...
