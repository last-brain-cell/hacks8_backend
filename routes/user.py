from fastapi import APIRouter, Body

from models.user import UserLocationUpdate, User

router = APIRouter()


@router.put("/update_location")
async def register(user_loc: UserLocationUpdate = Body(...)):
    user_exists = await User.find_one(User.email == user_loc.email)
    if user_exists:
        user_exists.location = user_loc.location
        await user_loc.save()
