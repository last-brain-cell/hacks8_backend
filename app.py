import certifi
import motor.motor_asyncio
import uvicorn
from beanie import init_beanie
from fastapi import FastAPI

import routes.announcement
import routes.disaster
import routes.login
import routes.report
import routes.user
from models.announcement import Announcement
from models.disaster import DisasterReport
from models.user import User

app = FastAPI()
# client = motor.motor_asyncio.AsyncIOMotorClient(
#     os.environ["MONGODB_URL"], tlsCAfile=certifi.where()
# )
client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb+srv://Naad:naad2002@cluster0.7redvzp.mongodb.net/",
    tlsCAfile=certifi.where(),
)

db = client.hacks8


@app.on_event("startup")
async def start_database():
    await init_beanie(database=db, document_models=[User, DisasterReport, Announcement])


app.include_router(routes.login.router, tags=["login"], prefix="/auth")
app.include_router(routes.report.router, tags=["report"], prefix="/disaster")
app.include_router(
    routes.announcement.router, tags=["announcement"], prefix="/announcement"
)
app.include_router(routes.disaster.router, tags=["disaster"], prefix="/disaster_ops")

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=80)
