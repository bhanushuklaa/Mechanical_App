from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
import enum

class VehicleType(str, enum.Enum):
    bike = "bike"
    car = "car"

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    type = Column(Enum(VehicleType), nullable=False)
