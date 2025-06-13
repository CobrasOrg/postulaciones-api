from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime
from enum import Enum


class Species(str, Enum):
    feline = "feline"
    canine = "canine"


class BloodType(str, Enum):
    DEA_1_1_POS = "DEA 1.1+"
    DEA_1_1_NEG = "DEA 1.1-"
    DEA_1_2 = "DEA 1.2"
    DEA_3 = "DEA 3"
    DEA_4 = "DEA 4"
    DEA_5 = "DEA 5"
    DEA_7 = "DEA 7"
    DEA_8 = "DEA 8"
    A = "A"
    B = "B"
    AB = "AB"



class ApplicationStatus(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"


class ApplicationCreate(BaseModel):
    petName: str = Field(..., example="Max")
    species: Species = Field(..., example="canine")
    breed: str = Field(..., example="Pastor Alemán")
    age: int = Field(..., example=3)
    weight: float = Field(..., example=25.0)
    bloodType: BloodType = Field(..., example="DEA 1.1+")
    lastVaccination: date = Field(..., example="2024-05-01")
    healthStatus: str = Field(..., example="Vacunas al día")
    medications: str = Field(..., example="Ninguno")
    ownerName: str = Field(..., example="Juan Pérez")
    ownerPhone: str = Field(..., example="+573001234567")
    ownerEmail: EmailStr = Field(..., example="juan.perez@email.com")
    ownerAddress: str = Field(..., example="Calle 100 #15-20, Bogotá")
    termsAccepted: bool = Field(..., example=True)


class ApplicationShort(BaseModel):
    id: str = Field(..., example="APP-001")
    petName: str = Field(..., example="Max")
    species: Species = Field(..., example="canine")
    breed: str = Field(..., example="Pastor Alemán")
    weight: float = Field(..., example=25.0)
    bloodType: BloodType = Field(..., example="DEA 1.1+")
    ownerName: str = Field(..., example="Juan Pérez")
    ownerPhone: str = Field(..., example="+573001234567")
    ownerEmail: EmailStr = Field(..., example="juan.perez@email.com")
    status: ApplicationStatus = Field(..., example="pending")


class ApplicationDetail(ApplicationShort):
    age: int = Field(..., example=3)
    lastVaccination: date = Field(..., example="2024-05-01")
    healthStatus: str = Field(..., example="Vacunas al día")
    medications: str = Field(..., example="Ninguno")
    ownerAddress: str = Field(..., example="Calle 100 #15-20, Bogotá")
    applicationDate: datetime = Field(..., example="2025-06-12T14:30:00")


class ApplicationStatusUpdate(BaseModel):
    status: ApplicationStatus = Field(..., example="approved")
