from typing import Annotated
import sqlalchemy
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from database.models import User
from services.user import UserService
from shemes.auth import UserRegister, UserLogin
from fastapi import Depends

from utils.auth_utils import hash_password, generate_token
from utils.dependens import user_service_fabric
from fastapi import HTTPException
auth_router = APIRouter(tags=['Auth'])


@auth_router.post('/token')
async def login(user: Annotated[OAuth2PasswordRequestForm, Depends()], user_service: Annotated[UserService, Depends(user_service_fabric)]):
    try:
        db_user: User = await user_service.get_user(user.username)
        if hash_password(user.password, db_user.salt) == db_user.hash_pass:
            return {"access_token": generate_token(db_user.username), "token_type": "bearer"}
        else:
            raise HTTPException(status_code=409, detail='Wrong password')
    except sqlalchemy.exc.NoResultFound:
        raise HTTPException(status_code=409, detail='This user did not exist')


@auth_router.post('/reg')
async def register(user: UserRegister, user_service: Annotated[UserService, Depends(user_service_fabric)]):
    try:
        await user_service.create_user(user)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=409, detail='This username or email already exist')
    return True