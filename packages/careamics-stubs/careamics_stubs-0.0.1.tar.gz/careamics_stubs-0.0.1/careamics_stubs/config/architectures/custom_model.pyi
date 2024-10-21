from .architecture_model import ArchitectureModel as ArchitectureModel
from .register_model import get_custom_model as get_custom_model
from _typeshed import Incomplete
from typing import Any, Literal
from typing_extensions import Self

class CustomModel(ArchitectureModel):
    model_config: Incomplete
    architecture: Literal['custom']
    name: str
    @classmethod
    def custom_model_is_known(cls, value: str) -> str: ...
    def check_parameters(self) -> Self: ...
    def model_dump(self, **kwargs: Any) -> dict[str, Any]: ...
