        *******************************
        ****                       ****
        ****        MANUAL         ****
        ****                       **** 
        *******************************

a. Program description:
        CLI chat room name based users gives username and room name to connect with each other

b. Running the program:
        1. have mongoDB online
        2. run restfulApi.py with 'python3 + restfulApi.py'
        3. run restfulClient with 'python3 + restfulClient'
        4. enjoy the chat.
        5. to leave your chat room press cntrl+C
        6. to kill the program press cntrl+C on login prompt.


c. disclaimer:
        1. prompt input limitations: only 5 seconds to give his text input.
           and then the server pull will reset his input can be fixed with another listener that will store 
           typed chars that wasnt sent and concat them to the empty string after the pull reset.
           or with the help of threading. (didnt implement cause socketing will solve the problem)  
        2. so far the program is only fulfilling the demands of the 4 first milestones (3 left).
        3. poor data managment - delete from data base and update exisiting values are not supported.
