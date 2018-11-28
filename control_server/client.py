import socket
from contextlib import closing
import sys

s = socket.socket()

host = sys.argv[1]
port = 8000

#with closing(s):
s.connect((host, port))
s.send(b"hi")
for _ in range(0, 100):
    print(host, s.recv(4096))
