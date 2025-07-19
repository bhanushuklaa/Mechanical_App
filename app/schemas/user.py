from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    service_boy = "service_boy"

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role: UserRole

class UserOut(UserBase):
    id: int
    role: UserRole

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
