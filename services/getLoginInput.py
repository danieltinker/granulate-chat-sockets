def loginValidation():
    room=""
    my_username=""
    proccess = True
    try:
        my_username = input("Username: ")
        room = input("RoomID: ")
    except(KeyboardInterrupt):
        proccess = False
        return((room,my_username,True,proccess))
    if(my_username=="" or room ==""):
        print("Invalid input(one of the fields is empty)...\nPlease try again\n")
        return (room,my_username,False,proccess)
    return (room,my_username,True,proccess)