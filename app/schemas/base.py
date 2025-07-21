from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from datetime import datetime

class ApplicationBase(BaseModel):
    petName: str
    species: Literal["canine", "feline"]
    breed: str
    age: int
    weight: float
    bloodType: str
    lastVaccination: datetime
    healthStatus: str
    ownerName: str
    ownerPhone: str
    ownerEmail: EmailStr
    ownerAddress: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    petPhoto: Optional[str] = None


class ApplicationShort(BaseModel):
    id: str
    petName: str
    ownerName: str
    ownerPhone: str
    ownerEmail: EmailStr
    species: Literal["canine", "feline"]
    breed: str
    age: int
    weight: float
    bloodType: str
    status: Literal["pending", "approved", "rejected"]
    createdAt: datetime


class ApplicationDetail(ApplicationBase):
    id: str
    solicitudId: str
    mascotaId: str
    ownerId: str
    status: Literal["pending", "approved", "rejected"]
    applicationDate: datetime
    createdAt: datetime
    updatedAt: datetime

class ApplicationStatusUpdate(BaseModel):
    status: Literal["approved", "rejected"]

class ApplicationStatusResponse(BaseModel):
    id: str
    status: Literal["approved", "rejected"]
    updatedAt: datetime

class ApplicationCreatedResponse(BaseModel):
    id: str
    solicitudId: str
    status: Literal["pending"]
    createdAt: datetime

