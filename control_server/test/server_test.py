import socket
from datetime import datetime
from time import sleep

s = socket.socket()

port = 8000
s.bind(('', port))

while True:
    print('listening')
    s.listen(5)
    c, addr = s.accept()
    print('receiving')
    
    while True:
        data = c.recv(4096).split(",")
        x = data[0]
        y = data[1]
        res = "Server recieved : x = " + str(x) + ", y = " + str(y)
        try:
            print(res)
        except:
            break
        sleep(1)
    c.close()
s.close()
