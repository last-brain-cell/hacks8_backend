import os

from beanie import init_beanie
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
import motor.motor_asyncio

from models.user import UserData, UserSignIn, User
from routes.login import router as login_router

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.hacks8


@app.on_event("startup")
async def start_database():
    await init_beanie(database=db, document_models=[User])


@app.post("/login", response_model=UserData)
async def login(login_creds: UserSignIn = Body(...)):
    print(login_creds)
    user_exists = await User.find_one(User.email == login_creds.email and User.password == login_creds.password)
    if user_exists:
        return user_exists
    raise HTTPException(status_code=403, detail="Incorrect email or password")


@app.post("/new", response_model=UserData)
async def login(user: User = Body(...)):
    user_exists = await User.find_one(User.email == user.email)
    if user_exists:
        raise HTTPException(
            status_code=409, detail="User with email supplied already exists"
        )
    return await user.create()
# app.include_router(login_router, tags=["login"], prefix="/admin")
