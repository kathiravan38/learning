"""only for start and stop the car then exit the game"""
started = False
while True:
    command = input(">>> ").lower()
    if command == "stop":
        if not started:
            print("car already stopped..")
        else:
            started = False
            print("car stopped.")
    elif command == "start":
        if started:
            print("car already started..")
        else:
            started = True
            print("car started...")
    elif command == "help":
        print("""start - starts the car
stop - stops the car
quit - to quit the game""")
    elif command == "quit":
        print("quiting...")
        break
    else:
        print("sorry, i don't understand ask help")