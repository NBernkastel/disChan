from pydantic import BaseModel
from pydantic import EmailStr


class UserLogin(BaseModel):
    username: str
    email: EmailStr
    password: str