from fastapi import FastAPI, Depends
from app.dependencies.auth import verify_token
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router

app = FastAPI(
    title="API de Postulaciones de Mascotas",
    dependencies=[Depends(verify_token)]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o lista específica
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
