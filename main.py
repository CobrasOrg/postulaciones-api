from fastapi import FastAPI, Depends, APIRouter
from app.dependencies.auth import verify_token
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="API de Postulaciones de Mascotas",
    version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router_protegido = APIRouter(dependencies=[Depends(verify_token)])
router_protegido.include_router(api_router)

app.include_router(router_protegido)

instrumentator = Instrumentator()
instrumentator.instrument(app)
instrumentator.expose(app, endpoint="/metrics", include_in_schema=False)