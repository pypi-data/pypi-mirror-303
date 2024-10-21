from ..config.support import SupportedActivation as SupportedActivation
from typing import Callable

def get_activation(activation: SupportedActivation | str) -> Callable: ...
