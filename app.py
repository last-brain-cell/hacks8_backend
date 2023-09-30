import os
import certifi
import motor.motor_asyncio
from beanie import init_beanie
from fastapi import FastAPI
from models.user import User
import routes.login
import routes.report

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(
    os.environ["MONGODB_URL"], tlsCAfile=certifi.where()
)
db = client.hacks8


@app.on_event("startup")
async def start_database():
    await init_beanie(database=db, document_models=[User])


app.include_router(routes.login.router, tags=["login"], prefix="/admin")