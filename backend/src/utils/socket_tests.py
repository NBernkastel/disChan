import asyncio
import websockets


async def send_data():
    uri = "ws://backend:8000/sockets/send_message"
    async with websockets.connect(uri) as websocket:
        await websocket.send(
            b'{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLmlkIjoxLCJleHAiOjE3MDEwMzg5MDF9.GRxYirb5M5CKvsA5jdKKelDW_DWQSFcE3XuRTRml9MM", "user_from": 1, "channel": 12, "server": 0, "body": "gg"}')
        resp = await websocket.recv()
        print(resp)
asyncio.get_event_loop().run_until_complete(send_data())
