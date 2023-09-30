from beanie import Document
from pydantic import BaseModel, EmailStr


class User(Document):
    fullname: str
    email: str
    password: str
    role: str

    class Settings:
        name = "user"


class UserSignIn(BaseModel):
    email: str
    password: str


class UserData(BaseModel):
    fullname: str
    email: EmailStr
    role: str
