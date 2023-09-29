from fastapi import Body, APIRouter, HTTPException
from models.user import User, UserSignIn, UserData

router = APIRouter()


@router.post("/login", response_model=UserData)
async def login(login_creds: UserSignIn = Body(...)):
    user_exists = await User.find_one(User.email == login_creds.email and User.password == login_creds.password)
    if user_exists:
        return user_exists
    raise HTTPException(status_code=403, detail="Incorrect email or password")


