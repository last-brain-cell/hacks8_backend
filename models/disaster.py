from typing import List

from beanie import Document, Link
from pydantic import BaseModel

from models.user import User


class DisasterReport(Document):
    disaster_id: str
    disaster_type: str
    location: str
    date: str
    description: str
    user: Link[User]
    verified: bool

    class Settings:
        name = "disaster_report"


class DisasterReportCreate(BaseModel):
    disaster_type: str
    location: List[float]
    date: str
    description: str
    reporter_id: str


class DisasterReportVerify(BaseModel):
    disaster_id: str
    verified: bool


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
