import socket
from commands import Rotate, Default
from servo import Servo
from controller import Controller
from time import sleep
import Queue

class Server(object):
    def __init__(self):
        self.servo = Servo()
        self.ctrl = Controller(self.servo)
        self.ctrl.execute(Default())
        print(self.servo)
        print(self.ctrl)

    def to_servo(self, x, y):
        """角度表記を信号幅に変換する
        Args:
            x (int): Android端末スクリーン上のx座標
            y (int): Android端末スクリーン上のy座標
        """
        cmd = Rotate(horizontal=x, vertical=y)
        self.ctrl.execute(cmd)
        print(cmd)
        
    def run(self):
        """サーバを起動する
        """
        s = socket.socket()

        port = 8000
        s.bind(('', port))

        while True:
            print('listening')
            s.listen(5)
            c, addr = s.accept()
            print('receiving')
            
            queue = Queue.Queue()
            while True:
                data = c.recv(4096)
                print(data)
                for d in data.split("\n"):
                    if d:
                        print(d)
                        queue.put(list(map(int, d.split(","))))
                        
                try:
                    if not queue.empty():
                        x, y = queue.get()
                        self.to_servo(x, y)
                except:
                    break
            c.close()
        s.close()
        
def main():
    server = Server()
    server.run()

if __name__=='__main__':
    main()
