from fastapi import Body, APIRouter, HTTPException

from models.user import User, UserSignIn, UserData

router = APIRouter()


@router.post("/login", response_model=UserData)
async def login(login_creds: UserSignIn = Body(...)):  # print(login_creds)
    print(login_creds)
    user_exists = await User.find_one(
        User.email == login_creds.email and User.password == login_creds.password
    )

    if user_exists:
        return user_exists
    raise HTTPException(status_code=403, detail="Invalid")


@router.post("/register", response_model=UserData)
async def register(user: User = Body(...)):
    user_exists = await User.find_one(User.email == user.email)
    if user_exists:
        raise HTTPException(status_code=409, detail=False)
    return await user.create()
