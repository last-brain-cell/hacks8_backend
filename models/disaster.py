from typing import List, Tuple
import datetime as dt
import pymongo
from beanie import Document
from pydantic import BaseModel


class GeoObject(BaseModel):
    type: str = "Point"
    coordinates: Tuple[float, float]


class DisasterReport(Document):
    disaster_id: int
    disaster_type: str
    location: GeoObject
    timestamp: dt.datetime
    description: str
    user: List[str]
    status: int = 0

    class Settings:
        name = "disaster"
        indexes = [
            [("location", pymongo.GEOSPHERE)],  # GEO index
        ]


class DisasterReportVerify(BaseModel):
    disaster_id: int
    status: int


class UserDisasterData(BaseModel):
    user: str
    disaster: DisasterReport


class VerifiedDisasters(BaseModel):
    disasters: List[DisasterReport]


