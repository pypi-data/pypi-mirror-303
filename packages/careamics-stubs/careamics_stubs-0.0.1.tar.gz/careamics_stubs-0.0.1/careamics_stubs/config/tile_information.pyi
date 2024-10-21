from _typeshed import Incomplete
from pydantic import BaseModel

DimTuple: Incomplete

class TileInformation(BaseModel):
    model_config: Incomplete
    array_shape: DimTuple
    last_tile: bool
    overlap_crop_coords: tuple[tuple[int, ...], ...]
    stitch_coords: tuple[tuple[int, ...], ...]
    sample_id: int
    def __eq__(self, other_tile: object): ...
