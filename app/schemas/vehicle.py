# app/schemas/vehicle.py

from pydantic import BaseModel, Field

class VehicleBase(BaseModel):
    name: str
    brand: str
    model: str
    year: int

class VehicleCreate(VehicleBase):
    pass

class VehicleOut(VehicleBase):
    id: int

    class Config:
        from_attributes = True  
