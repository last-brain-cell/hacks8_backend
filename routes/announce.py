from fastapi import Body, APIRouter

from models.announcement import Announcement

router = APIRouter()


@router.post("/announcement", response_model=Announcement)
async def create_announcement(announcement: Announcement = Body(...)):
    return "announcement announced"
