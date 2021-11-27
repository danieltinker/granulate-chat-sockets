import asyncio
import websockets
import requests

async def hello(username,roomname):
    async with websockets.connect("ws://localhost:8765/sub", extra_headers={"room_id": roomname,"name":username}) as websocket:
        while True:
            print(await websocket.recv())
            msg = input("listening: ")
            await websocket.send(msg)

username = input("please enter your usename: ")
roomname = input("please enter room name: ")
asyncio.run(hello(username,roomname))
