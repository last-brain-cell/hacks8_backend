from typing import Optional, Any
from beanie import Document
from pydantic import BaseModel, EmailStr
from fastapi.security import HTTPBasicCredentials


class User(Document):
    fullname: str
    email: EmailStr
    password: str
    role: str

    class Settings:
        name = "user"


class UserSignIn(BaseModel):
    email: EmailStr
    password: str


class UserData(BaseModel):
    fullname: str
    email: EmailStr
    role: str
