from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from endpoints.message_socket import socket_router
from endpoints.auth import auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(socket_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
