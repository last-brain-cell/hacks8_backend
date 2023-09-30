from beanie import Document, Link

from models.disaster import DisasterReport
from models.user import User


class Announcement(Document):
    user: Link[User]
    message: str
    event: Link[DisasterReport]

    class Settings:
        name = "announcement"
