from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise ValueError("MONGO_URL no está definido en el entorno.")

client = AsyncIOMotorClient(MONGO_URL)


db = client.get_default_database()

postulaciones_collection = db["postulaciones"]
