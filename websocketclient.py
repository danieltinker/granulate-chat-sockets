import asyncio
import time
import websockets
import requests
from pytimedinput import timedInput

BASE = "http://127.0.0.1:5000/"

async def rec(websocket):
    x=websocket.recv()
    await asyncio.sleep(1)
    return x

async def inputReq(websockets):
    return timedInput("<",3)

async def listen(username,roomname):
    async with websockets.connect("ws://localhost:8765/sub", extra_headers={"room_id": roomname,"name":username}) as websocket:
        while True:
            task1 = asyncio.create_task(inputReq(websocket))
            task2 = asyncio.create_task(rec(websocket))  
            value2 = await task2
            print(task2)
            websocket.send(task1)
            
            
        while True:
            textMsg = await websocket.recv()
            print(textMsg)
            inputMsg = input("listening: ")
            if(inputMsg==""):
                continue
            await websocket.send(inputMsg)

username = input("please enter your usename: ")
roomname = input("please enter room name: ")           
asyncio.run(listen(username,roomname))





