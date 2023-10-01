from typing import List, Tuple

import pymongo
from beanie import Document
from pydantic import BaseModel, EmailStr


class GeoObject(BaseModel):
    type: str = "Point"
    coordinates: Tuple[float, float]


class DisasterReport(Document):
    disaster_id: int
    disaster_type: str
    location: GeoObject
    date: str
    description: str
    user: EmailStr
    status: int = 0

    class Settings:
        name = "disaster"
        indexes = [
            [("location", pymongo.GEOSPHERE)],  # GEO index
        ]


class DisasterReportVerify(BaseModel):
    disaster_id: int
    status: int


class DisasterReportData(BaseModel):
    disaster_id: int
    disaster_type: str
    location: str
    date: str
    description: str
    reporter_id: str


class UserDisasterData(BaseModel):
    user: EmailStr
    disaster: DisasterReportData


class UserReportedDisasters(BaseModel):
    disasters: List[DisasterReportData]
