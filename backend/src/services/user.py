import pydantic_core

from database.models import User
from shemes.auth import UserRegister
from utils.repository import AbstractRepository
from utils.auth_utils import hash_password, generate_salt
from pydantic import EmailStr


class UserService:
    def __init__(self, repo: AbstractRepository):
        self.repo = repo()

    async def create_user(self, user: UserRegister):
        salt = generate_salt()
        db_user = {
            'username': user.username,
            'hash_pass': hash_password(user.password, salt),
            'salt': salt,
            'email': user.email
        }
        await self.repo.add_one(data=db_user)

    async def get_user(self, login):
        try:
            EmailStr._validate(login)
            return await self.repo.get_one(User.email == login)
        except pydantic_core._pydantic_core.PydanticCustomError:
            return await self.repo.get_one(User.username == login)
