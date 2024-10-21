from pydantic import BaseModel
from typing import Any

class ArchitectureModel(BaseModel):
    architecture: str
    def model_dump(self, **kwargs: Any) -> dict[str, Any]: ...
