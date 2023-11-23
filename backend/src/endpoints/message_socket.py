import json
from typing import Annotated

from services.message import MessageService
from utils.auth_utils import verify_token
from fastapi import APIRouter
from fastapi.websockets import WebSocket, WebSocketDisconnect
from fastapi import Depends

from utils.dependens import message_service_fabric

socket_router = APIRouter(prefix='/sockets', tags=['Websockets'])

active_connections = {}


@socket_router.websocket('/send_message')
async def sock(websocket: WebSocket, message_service: Annotated[MessageService, Depends(message_service_fabric)]):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            try:
                message = json.loads(data)
                print(message)
            except json.decoder.JSONDecodeError:
                print("Not valid json")
                await websocket.close(code=400)
                return False
            userid = verify_token(message['token'])
            if userid == message['user_from']:
                active_connections[message['user_from']] = [websocket, message['channel']]
                del message['token']
                await message_service.add_message(message)

    except WebSocketDisconnect:
        return False
