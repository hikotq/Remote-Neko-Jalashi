from instructions import Horizon, Vertical, Default
from servo import Servo
from controller import Controller

def main():
    servo = Servo()
    #servo.test()
    ctrl = Controller(servo)
    prog = [\
                Rotate(horizon=-90, deg=True),\
                Rotate(horizon=90, deg=True),\
                Default(),\
                Rotate(vertical=-90, deg=True),\
                Rotate(vertical=90, deg=True),\
                Default()\
            ]
    ctrl.execute_prog(prog)

if __name__=='__main__':
    main()
