from fastapi import APIRouter, HTTPException, Path
from typing import List
from app.schemas.base import (
    ApplicationCreate,
    ApplicationShort,
    ApplicationDetail,
    ApplicationStatusUpdate,
    Species,
)
from datetime import datetime

router = APIRouter()

fake_db: dict[str, list[ApplicationDetail]] = {}


@router.post(
    "/api/solicitudes/{id}/postulaciones",
    response_model=ApplicationShort,
    status_code=200,
    responses={
        200: {"description": "Respuesta exitosa."},
        400: {"description": "Datos inválidos."},
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


@router.get(
    "/api/solicitudes/{id}/postulaciones",
    response_model=List[ApplicationShort],
    responses={200: {"description": "Respuesta exitosa."},
               404: {"description": "No hay postulaciones para esta solicitud."}}
)
def list_applications(id: str):
    apps = fake_db.get(id)
    if not apps:
        raise HTTPException(status_code=404, detail="No hay postulaciones para la solicitud especificada.")
    return apps


@router.get(
    "/api/solicitudes/{id}/postulaciones/{postulacionId}",
    response_model=ApplicationDetail,
    responses={200: {"description": "Respuesta exitosa."},
               404: {"description": "Postulación no encontrada."}}
)
def get_application(id: str, postulacionId: str):
    apps = fake_db.get(id, [])
    for app in apps:
        if app.id == postulacionId:
            return app
    raise HTTPException(status_code=404, detail="Postulación no encontrada.")


@router.patch(
    "/api/solicitudes/{id}/postulaciones/{postulacionId}/status",
    response_model=ApplicationShort,
    responses={200: {"description": "Respuesta exitosa."},
               404: {"description": "Postulación no encontrada."}}
)
def update_application_status(id: str, postulacionId: str, status_update: ApplicationStatusUpdate):
    apps = fake_db.get(id, [])
    for app in apps:
        if app.id == postulacionId:
            app.status = status_update.status
            return app
    raise HTTPException(status_code=404, detail="Postulación no encontrada.")