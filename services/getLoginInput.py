def loginValidation():
    room=""
    my_username=""
    main_proccess = True
    try:
        my_username = input("Username: ")
        room = input("Room: ")
    except(KeyboardInterrupt):
        proccess = False
        return((room,my_username,True,main_proccess))
    if(my_username=="" or room ==""):
        print("Invalid input(one of the fields is empty)...\nPlease try again\n")
        return (room,my_username,False,main_proccess)
    return (room,my_username,True,main_proccess)