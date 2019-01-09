#-*-coding: utf-8-*-
from commands import Rotate

class Controller(object):
    def __init__(self, servo):
        self.servo = servo
        
    def execute_commands(self, commands):
        for cmd in commands:
            self.execute(cmd)

    def execute(self, cmd):
        if isinstance(cmd, Rotate):
            self.servo.rotate(vertical=cmd.vertical, horizontal=cmd.horizontal)
        else:
            self.servo.to_default()
