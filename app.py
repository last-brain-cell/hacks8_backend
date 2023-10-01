import certifi
import motor.motor_asyncio
import uvicorn
from beanie import init_beanie
from fastapi import FastAPI, WebSocket

import routes.announcement
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


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


@app.websocket("/ws/{client_id}")
def websocket_endpoint():
    pass


@app.on_event("startup")
async def start_database():
    await init_beanie(database=db, document_models=[User, DisasterReport, Announcement])


app.include_router(routes.login.router, tags=["login"], prefix="/auth")
app.include_router(routes.report.router, tags=["report"], prefix="/disaster")
app.include_router(
    routes.announcement.router, tags=["announcement"], prefix="/announcement"
)
app.include_router(routes.user.router, tags=["user"], prefix="/user")

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=80)
