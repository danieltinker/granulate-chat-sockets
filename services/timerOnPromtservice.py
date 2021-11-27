import requests
from pytimedinput import timedInput
import time

from restfulApi import Room 

def timerOnPrompt(BASE,room,my_username): 
    # def timedInput(prompt="", timeout=5, resetOnInput=True, maxLength=0, allowCharacters="", endCharacters="\x1b\n\r")
    userText, timedOut = timedInput("> ",5)
    if(timedOut):
        pass
    else:
        response = requests.put(BASE +'message',json={
            "roomname": room,
            "name": my_username,
            "msg" :  userText,
            "time": time.time()
            })
        if(response.ok):
            print("\nMessage Recieved\n\n\n")
    