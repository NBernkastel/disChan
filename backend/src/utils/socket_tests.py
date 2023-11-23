import asyncio
import websockets


async def send_data():
    uri = "ws://127.0.0.1:8000/sockets/send_message"
    async with websockets.connect(uri) as websocket:
        await websocket.send(
            b'{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLmlkIjoxLCJleHAiOjE3MDA0MzYyNTZ9'
            b'.CfCkLXzx3bxJaHUphJFl2omAJAud9rtyH8frAMlwUPs", "user_from": 1, "channel": 12, "server": 0, "body": "gg"}')


asyncio.get_event_loop().run_until_complete(send_data())
