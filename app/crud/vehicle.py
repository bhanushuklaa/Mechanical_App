from sqlalchemy.orm import Session
from app import models, schemas

def create_vehicle(db: Session, vehicle: schemas.vehicle.VehicleCreate):
    db_vehicle = models.vehicle.Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def get_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.vehicle.Vehicle).offset(skip).limit(limit).all()

def get_vehicle_by_id(db: Session, vehicle_id: int):
    return db.query(models.vehicle.Vehicle).filter(models.vehicle.Vehicle.id == vehicle_id).first()
