from instructions import Horizon, Vertical, Default
from servo import Servo
from controller import Controller

def main():
    servo = Servo()
    #servo.test()
    ctrl = Controller(servo)
    prog = [\
                Horizon(150),\
                Horizon(600),\
                Default(),\
                Vertical(150),\
                Vertical(600),\
                Default()\
            ]
    ctrl.execute_prog(prog)

if __name__=='__main__':
    main()
