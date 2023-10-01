from typing import Tuple, Optional

import pymongo
from beanie import Document
from pydantic import BaseModel


class GeoObject(BaseModel):
    type: str = "Point"
    coordinates: Tuple[float, float]


class User(Document):
    fullname: str
    email: str
    password: str
    role: str
    location: Optional[GeoObject] = None

    class Settings:
        name = "user"
        indexes = [
            [("location", pymongo.GEOSPHERE)],  # GEO index
        ]


class UserSignIn(BaseModel):
    email: str
    password: str


class UserData(BaseModel):
    fullname: str
    email: str
    role: str
    location: Optional[GeoObject] = None


class UserLocationUpdate(BaseModel):
    email: str
    location: GeoObject
