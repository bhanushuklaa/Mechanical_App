# app/schemas/vehicle.py
from pydantic import BaseModel
from enum import Enum

class VehicleType(str, Enum):
    bike = "bike"
    car = "car"

class VehicleBase(BaseModel):
    brand: str
    model: str
    type: VehicleType  

class VehicleCreate(VehicleBase):
    pass

class VehicleOut(VehicleBase):
    id: int

    class Config:
        from_attributes = True
