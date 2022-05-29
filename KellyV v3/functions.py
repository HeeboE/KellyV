import socket as s
import time as t
import sys
import threading
import queue as q

sys.path.insert(1, '/Users/ericjacobson/Documents/GitHub/KellyV/KellyV v3/payload')

victimQueue = q.Queue()

def startListener(lhost: str, lport: int, **kwargs):
    server = s.socket(s.AF_INET, s.SOCK_STREAM)
    server.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    server.bind((lhost, lport))
    server.listen(0)
    victim, victim_addr = server.accept()
    victimQueue.put((victim, victim_addr))

thr = threading.Thread(target=startListener, args=("localhost", 4444,))
thr.start()


def closeConnection(victim: s.SOCK_STREAM):
    victim.close()

v, va


v.send("i fart".encode())
t.sleep(5)
closeConnection(v)

