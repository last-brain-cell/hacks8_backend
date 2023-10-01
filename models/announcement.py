from beanie import Document


class Announcement(Document):
    user: str
    message: str
    event_id: int

    class Settings:
        name = "announcement"
