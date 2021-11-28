        *******************************
        ****                       ****
        ****        MANUAL         ****
        ****                       **** 
        *******************************

a. Program description:
        CLI chat room name based users gives username and room name to connect with each other

b. Running the program:
        1. ^have mongoDB online
        2. run restfulApi.py with 'python3 + restfulApi.py'
        3. run websocketserver.py
        4. run websocketclient.py (for non-socketing implementation run restfulClient.py) 
        4. enjoy the chat.
        5. to kill the program use cntrl + C

c. disclaimer:
        1. prompt limitations: on CLI while asking for input not refreshing recieved msgs properly
           since the loop is syncrounous. must press ENTER to see msgs recieved from the
           server.
        2. so far the program is fulfilling the demands of the 5 first milestones (no Bonuses
           e.g. no username has seen your message and authentication).
        3. fail connection to server error unhandled. 
        4. NO DockerFile!






^ mongo db online:
MacBook-Pro root path/ % sudo mkdir -p /System/Volumes/data/db 
MacBook-Pro root path/ % sudo chown -R `id -un` /System/Volumes/data/db
MacBook-Pro root path/ % sudo mongod --dbpath /System/Volumes/data/db