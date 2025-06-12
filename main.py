from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router

app = FastAPI(
    title="API de Postulaciones de Mascotas"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o lista específica
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
