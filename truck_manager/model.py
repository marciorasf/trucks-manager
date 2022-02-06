from typing import Literal, NewType
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field, PositiveInt

TruckId = NewType("TruckId", UUID4)


class Truck(BaseModel):
    identifier: TruckId = TruckId(uuid4())
    plate: str = Field(..., min_length=1, max_length=7)
    model_name: str = Field(..., min_length=1, max_length=20)
    tank_capacity: PositiveInt
    status: Literal["OK", "ON_MAINTENANCE", "BROKEN"]

    class Config:
        allow_mutation = False
