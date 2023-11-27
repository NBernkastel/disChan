from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from services.user import UserService
from utils.auth_utils import auth_user
from utils.dependens import user_service_fabric, user_to_user_fabric

user_router = APIRouter(prefix='/user', tags=['User'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@user_router.get('/current')
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],
                           user_service: Annotated[UserService, Depends(user_service_fabric)]):
    username = auth_user(token)
    user = await user_service.get_user(username)
    del user.hash_pass
    del user.salt
    return user


@user_router.get('/friends')
async def get_user_friends(token: Annotated[str, Depends(oauth2_scheme)],
                           user_service: Annotated[UserService, Depends(user_to_user_fabric)]):
    username = auth_user(token)
    friends = await user_service.get_user_friends(username)
    return friends
