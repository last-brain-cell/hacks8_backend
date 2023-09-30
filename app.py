import os

import certifi
import motor.motor_asyncio
from beanie import init_beanie
from fastapi import FastAPI

import routes.announce
import routes.login
import routes.report
from models.announcement import Announcement
from models.disaster import DisasterReport
from models.user import User

app = FastAPI()
# client = motor.motor_asyncio.AsyncIOMotorClient(
#     os.environ["MONGODB_URL"], tlsCAfile=certifi.where()
# )
client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb+srv://Naad:naad2002@cluster0.7redvzp.mongodb.net/", tlsCAfile=certifi.where()
)

db = client.hacks8


@app.on_event("startup")
async def start_database():
    await init_beanie(database=db, document_models=[User, DisasterReport, Announcement])


app.include_router(routes.login.router, tags=["login"], prefix="/admin")
app.include_router(routes.report.router, tags=["login"], prefix="/admin")
app.include_router(routes.announce.router, tags=["login"], prefix="/admin")
