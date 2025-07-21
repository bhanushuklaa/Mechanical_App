from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.vehicle import VehicleCreate, VehicleOut
from app.crud import vehicle as crud_vehicle
from app.dependencies import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=VehicleOut)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return crud_vehicle.create_vehicle(db, vehicle)

@router.get("/", response_model=List[VehicleOut])
def read_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_vehicle.get_vehicles(db, skip, limit)

@router.get("/{vehicle_id}", response_model=VehicleOut)
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = crud_vehicle.get_vehicle_by_id(db, vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle
