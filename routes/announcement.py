from beanie.odm.operators.find.geospatial import Near
from fastapi import APIRouter, HTTPException, Query, Body

from models.announcement import Announcement
from models.disaster import DisasterReport
from models.user import UserLocationUpdate

router = APIRouter()


async def send_text_notification(user_token, message):
    try:
        print(f"Text notification sent to {user_token} Bhaago Bhaago Toofan aya")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Notification error: {str(e)}")


@router.get("/nearby_users")
async def get_nearby_users_for_disaster(
    disaster_id: str = Query(
        ..., description="The ID of the disaster for which to find nearby users"
    )
):
    disaster = await DisasterReport.find_one(DisasterReport.disaster_id == disaster_id)
    if not disaster:
        raise HTTPException(status_code=404, detail="Disaster not found")

    max_distance = 100

    nearby_users = await UserLocationUpdate.find(
        Near(
            UserLocationUpdate.location,
            disaster.location[0],
            disaster.location[1],
            max_distance=max_distance,
        )
    )
    return {"nearby_users": nearby_users}


async def send_announcement_to_nearby_users(announcement: Announcement):
    disaster_location = announcement.location
    max_distance = 100
    nearby_users = await UserLocationUpdate.find(
        Near(
            UserLocationUpdate.location,
            disaster_location[0],
            disaster_location[1],
            max_distance=max_distance,
        )
    )

    for user in nearby_users:
        user_token = user.notification_token
        message = announcement.message
        await send_text_notification(user_token, message)


@router.post("/announcement", response_model=Announcement)
async def create_announcement(announcement: Announcement = Body(...)):
    await send_announcement_to_nearby_users(announcement)
    return announcement
