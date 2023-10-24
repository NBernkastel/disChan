from typing import Annotated
import sqlalchemy
from fastapi import APIRouter
from services.user import UserService
from shemes.auth import User
from fastapi import Depends
from utils.dependens import user_service_fabric
from fastapi import HTTPException
auth_router = APIRouter(prefix='/auth', tags=['Auth'])


@auth_router.post('/log')
async def login(user: User):
    pass


@auth_router.post('/reg')
async def register(user: User, user_service: Annotated[UserService, Depends(user_service_fabric)]):
    try:
        await user_service.create_user(user)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=409, detail='This username or email already exist')
    return True
