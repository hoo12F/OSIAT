# Licensed under the MIT License <https://opensource.org/licenses/MIT>
# Copyright (c) 2022, Shoops

import socket
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

while True:
    cmd = input("[~] $ ")
    if cmd == 'launch twttr':
        print("Twitter")
        print("tacobell23912: I think that BTS is overated.")
        print("ninjastar12: stfu")
        print("youretrash: yeah i agree")
        print("jiminsimp902: your ip address is " + host_ip + " mf")
        print("sugasupremacy: no one asked lmao BTS is better than you")
        tweet = input("tweet something: ")
        print("You: " + tweet)

    if cmd == 'launch msngr':
        print("Messenger")
        print("mom >  |   mom: WHY DID YOU GET 1 WRONG ON THE TEST.")
        print("dad    |   you: I CAN EXPLAIN OK")
        print("aunt   |   mom: i dont want to hear it.")
        print("       |   you: MOM PLEASE HAVE MERCY")
        print("       |   mom: COME DOWN HERE RIGHT THIS INSTANT.")
        msg = input("       |   send something: ")
        print("       |   You: " + msg)

    if cmd == 'launch vscode':
        print("haha here's a crappy text editor instead")
    if cmd == 'help':
        print("adding a help command?? nah, im too lazy to. just look at the source code")

    if cmd == 'info':
        print("Copyright (c) Shoops ")
        print("Software name: OSIAT")
        print("License: MIT")

    if cmd == 'mkdir':
        input("name your directory: ")
        print("JUST KIDDING IM NOT MAKING A MKDIR COMMAND THATS TOO MUCH WORK!!!")