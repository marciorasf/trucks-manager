from typing import Literal

from pydantic import BaseModel, Field, PositiveInt


class Truck(BaseModel):
    plate: str = Field(..., min_length=1, max_length=7)
    model_name: str = Field(..., min_length=1, max_length=20)
    tank_capacity: PositiveInt
    status: Literal["OK", "ON_MAINTENANCE", "BROKEN"]

    class Config:
        allow_mutation = False
