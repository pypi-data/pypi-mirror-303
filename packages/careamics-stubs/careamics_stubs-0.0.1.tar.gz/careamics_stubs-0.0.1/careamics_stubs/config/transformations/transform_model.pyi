from _typeshed import Incomplete
from pydantic import BaseModel
from typing import Any

class TransformModel(BaseModel):
    model_config: Incomplete
    name: str
    def model_dump(self, **kwargs) -> dict[str, Any]: ...
