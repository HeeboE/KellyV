import socket as s

connection = s.socket()

connection.connect(("localhost", 4444))

while True:
    recv = connection.recv(10).decode()
    print(recv)