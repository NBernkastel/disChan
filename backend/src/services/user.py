from utils.repository import AbstractRepository


class UserService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo() 
    