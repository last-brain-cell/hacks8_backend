from beanie import Document


class Announcement(Document):
    user: str
    message: str
    disaster_id: int

    class Settings:
        name = "announcement"
