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

from app.db.database import postulaciones_collection
import uuid

router = APIRouter()


@router.get(
    "/solicitudes/{solicitud_id}/postulaciones",
    response_model=List[ApplicationShort],
    status_code=status.HTTP_200_OK,
)

async def get_postulaciones(solicitud_id: str):
    cursor = postulaciones_collection.find({"solicitudId": solicitud_id})
    docs = await cursor.to_list(length=None)
    return [ApplicationShort(**doc) for doc in docs]



@router.get(
    "/solicitudes/{solicitud_id}/postulaciones/{postulacion_id}",
    response_model=ApplicationDetail,
    status_code=status.HTTP_200_OK,
)

async def get_postulacion(solicitud_id: str, postulacion_id: str):
    doc = await postulaciones_collection.find_one({
        "solicitudId": solicitud_id,
        "id": postulacion_id
    })
    if not doc:
        raise HTTPException(status_code=404, detail="Postulación no encontrada")
    return ApplicationDetail(**doc)



@router.patch(
    "/solicitudes/{solicitud_id}/postulaciones/{postulacion_id}/status",
    response_model=ApplicationStatusResponse,
    status_code=status.HTTP_200_OK,

)

async def update_postulacion_status(solicitud_id: str, postulacion_id: str, payload: ApplicationStatusUpdate):
    updated_at = datetime.utcnow()
    result = await postulaciones_collection.find_one_and_update(
        {"solicitudId": solicitud_id, "id": postulacion_id},
        {"$set": {"status": payload.status, "updatedAt": updated_at}},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=404, detail="Postulación no encontrada")
    return ApplicationStatusResponse(id=result["id"], status=result["status"], updatedAt=result["updatedAt"])


@router.post(
    "/solicitudes/{solicitud_id}/postulaciones",
    response_model=ApplicationCreatedResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_postulacion(solicitud_id: str, body: ApplicationCreate):
    existing = await postulaciones_collection.find_one({
        "solicitudId": solicitud_id,
        "ownerEmail": body.ownerEmail
    })
    if existing:
        raise HTTPException(status_code=409, detail="Ya existe una postulación con este correo electrónico.")

    count = await postulaciones_collection.count_documents({"solicitudId": solicitud_id})
    new_id = str(uuid.uuid4())
    now = datetime.utcnow()

    doc = {
        "id": new_id,
        "solicitudId": solicitud_id,
        "mascotaId": "pet_" + new_id,
        "ownerId": "owner_" + new_id,
        "status": "pending",
        "applicationDate": now,
        "createdAt": now,
        "updatedAt": now,
        **body.dict(),
    }

    await postulaciones_collection.insert_one(doc)

    return ApplicationCreatedResponse(
        id=new_id,
        solicitudId=solicitud_id,
        status="pending",
        createdAt=now
    )

