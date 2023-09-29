from fastapi import APIRouter
from models.users import Users
from schema.schemas import list_serial
from config.database import users_collections
from bson import ObjectId

router = APIRouter()

@router.get("/users")
async def get_users():
    # if users_collections.find(username) and password == users_collections.find(username)['password']:
    #     return "logged in"
    # else:
    #     return "login failed"
    return users_collections.find()
