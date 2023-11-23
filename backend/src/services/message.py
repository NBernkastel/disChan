from utils.repository import AbstractRepository


class MessageService:
    def __init__(self, repo: AbstractRepository):
        self.repo = repo()

    async def add_message(self, message: dict):
        await self.repo.add_one(message)
