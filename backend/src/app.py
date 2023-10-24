from fastapi import FastAPI

from endpoints.auth import auth_router

app = FastAPI()

app.include_router(auth_router)
