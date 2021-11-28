import asyncio
import time
import websockets
import requests
BASE = "http://127.0.0.1:5000/"
async def listen(username,roomname):
    async with websockets.connect("ws://localhost:8765/sub", extra_headers={"room_id": roomname,"name":username}) as websocket:
          
        while True:
            textMsg = await websocket.recv()
            print(textMsg)
            inputMsg = input("listening: ")
            await websocket.send(inputMsg)

username = input("please enter your usename: ")
roomname = input("please enter room name: ")           
asyncio.run(listen(username,roomname))





