from typing import Literal, NewType
from uuid import uuid4

from pydantic import BaseModel, Field, PositiveInt

TruckId = NewType("TruckId", str)


def parse_truck_id(value: str) -> TruckId:
    """All TruckIds must be created using this function."""
    return TruckId(value)


class Truck(BaseModel):
    identifier: TruckId = parse_truck_id(str(uuid4()))
    plate: str = Field(..., min_length=1, max_length=7)
    model_name: str = Field(..., min_length=1, max_length=20)
    tank_capacity: PositiveInt
    status: Literal["OK", "ON_MAINTENANCE", "BROKEN"]

    class Config:
        allow_mutation = False
        frozen = True
