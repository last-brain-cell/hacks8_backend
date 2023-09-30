from typing import List, Tuple

import pymongo
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from models.user import User

class GeoObject(BaseModel):
    type: str = "Point"
    coordinates: Tuple[float, float]

class DisasterReport(Document):
    disaster_id: str
    disaster_type: str
    location: GeoObject
    date: str
    description: str
    user: EmailStr
    verified: bool = False

    class Settings:
        name = "disaster"
        indexes = [
            [("location", pymongo.GEOSPHERE)],  # GEO index
        ]


class DisasterReportVerify(BaseModel):
    disaster_id: str

class DisasterReportData(BaseModel):
    disaster_id: str
    disaster_type: str
    location: str
    date: str
    description: str
    reporter_id: str


class UserDisasterData(BaseModel):
    user: Link[User]
    disaster: DisasterReportData


class UserReportedDisasters(BaseModel):
    disasters: List[DisasterReportData]
