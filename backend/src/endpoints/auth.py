from fastapi import APIRouter

from shemes.auth import UserLogin

auth_router = APIRouter(prefix='/auth', tags=['Auth'])



auth_router.post('/login')
async def login(user: UserLogin):
    pass