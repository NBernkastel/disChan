from fastapi import APIRouter
from fastapi.websockets import WebSocket, WebSocketDisconnect
import sounddevice as sd
import numpy as np

socket_router = APIRouter(prefix='/sockets', tags=['Websockets'])


@socket_router.websocket('/test')
async def sock(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            audio_data = await websocket.receive_bytes()
            audio_data = np.frombuffer(audio_data, dtype=np.int32)
            sd.play(audio_data, samplerate=48000)
            sd.wait()
            await websocket.send_text("ok")
    except WebSocketDisconnect:
        sd.stop()
