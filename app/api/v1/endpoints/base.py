from fastapi import APIRouter, HTTPException, Path, status, Depends
from typing import List
from datetime import datetime
from app.schemas.base import (
    ApplicationCreate,
    ApplicationShort,
    ApplicationDetail,
    ApplicationStatusUpdate,
    ApplicationStatusResponse,
    ApplicationCreatedResponse,
)

router = APIRouter()

fake_db: dict[str, list[ApplicationDetail]] = {}


@router.get(
    "/solicitudes/{solicitud_id}/postulaciones",
    response_model=List[ApplicationShort],
    status_code=status.HTTP_200_OK,
)
def get_postulaciones(solicitud_id: str):
    return fake_db.get(solicitud_id, [])


@router.get(
    "/solicitudes/{solicitud_id}/postulaciones/{postulacion_id}",
    response_model=ApplicationDetail,
    status_code=status.HTTP_200_OK,
)
def get_postulacion(solicitud_id: str, postulacion_id: str):
    postulaciones = fake_db.get(solicitud_id, [])
    for p in postulaciones:
        if p.id == postulacion_id:
            return p
    raise HTTPException(status_code=404, detail="Postulación no encontrada")


@router.patch(
    "/solicitudes/{solicitud_id}/postulaciones/{postulacion_id}/status",
    response_model=ApplicationStatusResponse,
    status_code=status.HTTP_200_OK,
)
def update_postulacion_status(solicitud_id: str, postulacion_id: str, payload: ApplicationStatusUpdate):
    postulaciones = fake_db.get(solicitud_id, [])
    for i, p in enumerate(postulaciones):
        if p.id == postulacion_id:
            p.status = payload.status
            p.updatedAt = datetime.utcnow()
            fake_db[solicitud_id][i] = p
            return ApplicationStatusResponse(id=p.id, status=p.status, updatedAt=p.updatedAt)
    raise HTTPException(status_code=404, detail="Postulación no encontrada")


@router.post(
    "/solicitudes/{solicitud_id}/postulaciones",
    response_model=ApplicationCreatedResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_postulacion(solicitud_id: str, body: ApplicationCreate):
    # Validación de email duplicado
    for p in fake_db.get(solicitud_id, []):
        if p.ownerEmail == body.ownerEmail:
            raise HTTPException(status_code=409, detail="Ya existe una postulación con este correo electrónico.")

    new_id = f"app_{len(fake_db.get(solicitud_id, [])) + 1}"
    now = datetime.utcnow()
    new_postulacion = ApplicationDetail(
        id=new_id,
        solicitudId=solicitud_id,
        mascotaId="pet_" + new_id,
        ownerId="owner_" + new_id,
        status="pending",
        applicationDate=now,
        createdAt=now,
        updatedAt=now,
        **body.dict(),
    )

    fake_db.setdefault(solicitud_id, []).append(new_postulacion)
    return ApplicationCreatedResponse(id=new_id, solicitudId=solicitud_id, status="pending", createdAt=now)
