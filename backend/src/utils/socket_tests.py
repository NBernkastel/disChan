import asyncio
import websockets
from pydub import AudioSegment


async def send_data():
    sapmle_len = 3000
    audio = AudioSegment.from_file('../hello.mp3')
    chunk_count = len(audio) // sapmle_len
    uri = "ws://127.0.0.1:8000/sockets/test"
    async with websockets.connect(uri) as websocket:
        for i in range(chunk_count):
            start_time = i * sapmle_len
            end_time = (i + 1) * sapmle_len
            print(i)
            audio_chunk = audio[start_time:end_time]
            message = audio_chunk.raw_data
            await websocket.send(message)
            await websocket.recv()


asyncio.get_event_loop().run_until_complete(send_data())
