import datetime
import random
from typing import List, Tuple

import pymongo
from beanie import Document
from pydantic import BaseModel


class GeoObject(BaseModel):
    type: str = "Point"
    coordinates: Tuple[float, float]


class DisasterReport(Document):
    disaster_id: int = random.randint(0, 1000000000)
    disaster_type: str
    location: GeoObject
    timestamp: datetime.datetime = datetime.datetime.now()
    description: str
    user: str
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
