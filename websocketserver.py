import asyncio
import websockets
import requests
import time
BASE = "http://127.0.0.1:5000/"
connections = set()
n = 0

def getchathistory(websocket,room_id):
    response = requests.get(BASE+'message',{"roomname":room_id})
    if(response.ok):
        if(response.status_code==204):
            asyncio.ensure_future(websocket.send("empty chat"))
        else:
            asyncio.ensure_future(websocket.send(response.json()['msgs']))
            for msg in response.json()['msgs']:
                print(msg)
                       
                        
async def handler(websocket, path):
    
    global n
    if path == "/sub":
        n = n + 1
        i = n
        connections.add(websocket)
        name = websocket.request_headers.get("name")
        room_id = websocket.request_headers.get("room_id")
        # if(room_id ==None or name ==None or name ==""or room_id ==""):
        #     asyncio.ensure_future(ws.send("Invalid input: no name or room was given "))
        # else:    
        print("adding subscriber #", name)
        getchathistory(websocket,room_id)
        async for msg in websocket:
            name = websocket.request_headers.get("name")
            room_id = websocket.request_headers.get("room_id")
            print(name,":", msg)
            response = requests.put(BASE +'message',json={
                "roomname": room_id,
                "name": name,
                "msg" :  msg,
                "time": time.time()
                })
        
            for ws in connections:
                ws_room_id = ws.request_headers.get("room_id")
                if ws_room_id == room_id:
                    response = requests.put(BASE + 'room/'+room_id,json={
                "room": room_id,
                "name": name
                })
                    asyncio.ensure_future(ws.send(name +": "+ msg))

start_server = websockets.serve(handler, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
