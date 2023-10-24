from shemes.auth import User
from utils.repository import AbstractRepository
from utils.auth_utils import hash_password, generate_salt


class UserService:
    def __init__(self, repo: AbstractRepository):
        self.repo = repo()

    async def create_user(self, user: User):
        salt = generate_salt()
        db_user = {
            'username': user.username,
            'hash_pass': hash_password(user.password, salt),
            'salt': salt,
            'email': user.email
        }
        print(db_user)
        await self.repo.add_one(data=db_user)
