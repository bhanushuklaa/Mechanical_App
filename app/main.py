from fastapi import FastAPI
from app.database import Base, engine
from app.api.v1 import auth, users, vehicles, services, bookings, inventory

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mechanical Store API")

# Include Routers
app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(users.router, prefix="/api/v1/users")
app.include_router(vehicles.router, prefix="/api/v1/vehicles")
app.include_router(services.router, prefix="/api/v1/services")
app.include_router(bookings.router, prefix="/api/v1/bookings")
app.include_router(inventory.router, prefix="/api/v1/inventory")
