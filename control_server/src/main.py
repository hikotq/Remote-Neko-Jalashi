from commands import Rotate, Default
from servo import Servo
from controller import Controller

def main():
    servo = Servo()
    #servo.test()
    ctrl = Controller(servo)
    cmd = [\
                Rotate(horizontal=-90, deg=True),\
                Rotate(horizontal=90, deg=True),\
                Default(),\
                Rotate(vertical=-90, deg=True),\
                Rotate(vertical=90, deg=True),\
                Default()\
            ]
    ctrl.execute_commands(cmd)

if __name__=='__main__':
    main()
