import json
from typing import Annotated
from services.message import MessageService
from fastapi import APIRouter
from fastapi.websockets import WebSocket, WebSocketDisconnect
from fastapi import Depends

from utils.auth_utils import verify_token
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
            except json.decoder.JSONDecodeError:
                await websocket.close(code=400)
                return False
            userid = verify_token(message['token'])
            if userid == message['user_from']:
                if message['channel'] in active_connections:
                    active_connections[message['channel']].append(websocket)
                else:
                    active_connections[message['channel']] = [websocket]
                for ws in active_connections[message['channel']]:
                    await ws.send_text(message['body'])
                del message['token']
                await message_service.add_message(message)

    except WebSocketDisconnect:
        return False
