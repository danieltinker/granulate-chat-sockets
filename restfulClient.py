import requests
import time
from pytimedinput import timedInput
from services.getLoginInput import loginValidation
from services.timerOnPromtservice import timerOnPrompt

BASE = "http://127.0.0.1:5000/"

isValid=False
isServerOn=False
proccess=True
while proccess:
    try:
        response = requests.get(BASE+'/isON')
        if response:
            print("*** server is CONNECTED ***,\n Welcome to CHAT by daniel\n to switch between rooms please click cntrl+C\n")
            while(not isValid):
                    (room,my_username,isValid,proccess)=loginValidation()
            if(proccess==False):
                break
            try:  
                #room & user setup
                response = requests.put(BASE + 'room/'+room,json={
                    "room": room,
                    "name": my_username
                    })
                
                #listen to msgs endless loop -> improve to socket communication
                while True:
                    timerOnPrompt(BASE,room,my_username)
                    response = requests.get(BASE+'message',{"roomname":room})
                    if(response.ok):
                        if(response.status_code==204):
                            print("chat is empty")
                        else:
                            for msg in response.json()['msgs']:
                                print(msg)
                    else:
                        print("couldnt pull chat from server")
                        
            #Control+C handle        
            except KeyboardInterrupt:
                print("Goodbye " + my_username)
                isValid=False
            
            finally:
                
                response = requests.put(BASE +'message',json={
                        "roomname": room,
                        "name": my_username,
                        "msg" : my_username + ' Has left the chatroom.',
                        "time": time.time()
                        })
                
    except Exception as e:
        print("looking for server...")
        
    except KeyboardInterrupt:
        proccess=False

print("Thanks for using CHAT by daniel")