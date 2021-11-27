import asyncio
import websockets
import requests
import time
BASE = "http://127.0.0.1:5000/"
connections = set()
n = 0

# async def printchathistory(websocket):
#         room_id = websocket.request_headers.get("room_id")
#         async for ws in connections:
#             ws_room_id = ws.request_headers.get("room_id")
#             if ws_room_id == room_id:
#                 await(ws.send("WELCOME,print the fucking history"))
    
async def handler(websocket, path):
    global n

    if path == "/sub":
        n = n + 1
        i = n
        connections.add(websocket)
        name = websocket.request_headers.get("name")
        room_id = websocket.request_headers.get("room_id")
        print("adding subscriber #", name)
        
        if websocket in connections:
            for ws in connections:
                ws_name_temp = ws.request_headers.get("name")
                if ws_name_temp == name:
                    response = requests.get(BASE+'message',{"roomname":room_id})
                    if(response.ok):
                        if(response.status_code==204):
                            asyncio.ensure_future(ws.send("empty chat"))
                        else:
                            for msg in response.json()['msgs']:
                                print(msg)
                                asyncio.ensure_future(ws.send(msg))
                    
        if websocket not in connections:
            try:
                async for msg in websocket:
                    pass  # ignore
            except websockets.ConnectionClosed:
                pass
            finally:
                print("removing subscriber #", i)
                #print to clients in room that user name left the room PUT to msgs
                connections.remove(websocket)
        else:
            async for msg in websocket:
                print("<", msg)
                name = websocket.request_headers.get("name")
                room_id = websocket.request_headers.get("room_id")
                for ws in connections:
                    ws_room_id = ws.request_headers.get("room_id")
                    if ws_room_id == room_id:
                        response = requests.put(BASE + 'room/'+room_id,json={
                    "room": room_id,
                    "name": name
                    })
                        response = requests.put(BASE +'message',json={
                    "roomname": room_id,
                    "name": name,
                    "msg" :  msg,
                    "time": time.time()
            })
                        print(msg)
                        asyncio.ensure_future(ws.send(name +": "+ msg))

start_server = websockets.serve(handler, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()