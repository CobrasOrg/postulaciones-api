<<<<<<< Updated upstream
from fastapi import APIRouter, HTTPException, Path
from typing import List
=======
from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime

>>>>>>> Stashed changes
from app.schemas.base import (
    ApplicationCreate,
    ApplicationShort,
    ApplicationDetail,
    ApplicationStatusUpdate,
    Species,
)
from datetime import datetime

from app.db.database import postulaciones_collection

router = APIRouter()

<<<<<<< Updated upstream
fake_db: dict[str, list[ApplicationDetail]] = {}


@router.post(
    "/api/solicitudes/{id}/postulaciones",
    response_model=ApplicationShort,
    status_code=200,
    responses={
        200: {"description": "Respuesta exitosa."},
        409: {"description": "Ya existe una postulación con ese correo."},
        422: {"description": "Tipo de sangre no compatible."},
    },
)
def create_application(id: str, application: ApplicationCreate):
    # Validar que no exista otra postulación del mismo dueño (por email)
    existing_apps = fake_db.get(id, [])
    for app in existing_apps:
        if app.ownerEmail == application.ownerEmail:
            raise HTTPException(
                status_code=409,
                detail=f"Ya existe una postulación del correo {application.ownerEmail} para la solicitud {id}."
            )

    # Crear nueva postulación
    app_id = f"APP-{len(existing_apps) + 1:03}"
    app_data = ApplicationDetail(
        id=app_id,
        applicationDate=datetime.utcnow(),
        status="pending",
        **application.dict()
    )
    fake_db.setdefault(id, []).append(app_data)

    return app_data


=======
>>>>>>> Stashed changes
@router.get(
    "/api/solicitudes/{id}/postulaciones",
    response_model=List[ApplicationShort],
    responses={200: {"description": "Respuesta exitosa."},
               422: {"description": "Error de validación."},
               404: {"description": "No hay postulaciones para esta solicitud."}}
)
<<<<<<< Updated upstream
def list_applications(id: str):
    apps = fake_db.get(id)
    if not apps:
        raise HTTPException(status_code=404, detail="No hay postulaciones para la solicitud especificada.")
    return apps
=======
async def get_postulaciones(solicitud_id: str):
    cursor = postulaciones_collection.find({"solicitudId": solicitud_id})
    return await cursor.to_list(length=100)
>>>>>>> Stashed changes


@router.get(
    "/api/solicitudes/{id}/postulaciones/{postulacionId}",
    response_model=ApplicationDetail,
    responses={200: {"description": "Respuesta exitosa."},
               422: {"description": "Error de validación"},
               404: {"description": "Postulación no encontrada."}}
)
<<<<<<< Updated upstream
def get_application(id: str, postulacionId: str):
    apps = fake_db.get(id, [])
    for app in apps:
        if app.id == postulacionId:
            return app
    raise HTTPException(status_code=404, detail="Postulación no encontrada.")
=======
async def get_postulacion(solicitud_id: str, postulacion_id: str):
    postulacion = await postulaciones_collection.find_one({
        "solicitudId": solicitud_id,
        "id": postulacion_id
    })
    if not postulacion:
        raise HTTPException(status_code=404, detail="Postulación no encontrada")
    return postulacion
>>>>>>> Stashed changes


@router.patch(
    "/api/solicitudes/{id}/postulaciones/{postulacionId}/status",
    response_model=ApplicationShort,
    responses={200: {"description": "Respuesta exitosa."},
               422: {"description": "Error de validación"},
               404: {"description": "Postulación no encontrada."}}
               
)
<<<<<<< Updated upstream
def update_application_status(id: str, postulacionId: str, status_update: ApplicationStatusUpdate):
    apps = fake_db.get(id, [])
    for app in apps:
        if app.id == postulacionId:
            app.status = status_update.status
            return app
    raise HTTPException(status_code=404, detail="Postulación no encontrada.")
=======
async def update_postulacion_status(solicitud_id: str, postulacion_id: str, payload: ApplicationStatusUpdate):
    now = datetime.utcnow()
    result = await postulaciones_collection.update_one(
        {"solicitudId": solicitud_id, "id": postulacion_id},
        {"$set": {"status": payload.status, "updatedAt": now}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Postulación no encontrada")

    return ApplicationStatusResponse(id=postulacion_id, status=payload.status, updatedAt=now)


@router.post(
    "/solicitudes/{solicitud_id}/postulaciones",
    response_model=ApplicationCreatedResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_postulacion(solicitud_id: str, body: ApplicationCreate):
    # Validación de email duplicado
    existe = await postulaciones_collection.find_one({
        "solicitudId": solicitud_id,
        "ownerEmail": body.ownerEmail
    })
    if existe:
        raise HTTPException(status_code=409, detail="Ya existe una postulación con este correo electrónico.")

    now = datetime.utcnow()
    new_id = f"app_{int(now.timestamp() * 1000)}"
    nueva_postulacion = {
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

    await postulaciones_collection.insert_one(nueva_postulacion)

    return ApplicationCreatedResponse(
        id=new_id,
        solicitudId=solicitud_id,
        status="pending",
        createdAt=now
    )
>>>>>>> Stashed changes
