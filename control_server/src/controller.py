#-*-coding: utf-8-*-
from commands import Rotate

class Controller(object):
    """サーボを操作するクラス
    """
    def __init__(self, servo):
        self.servo = servo
        
    def execute_commands(self, commands):
        """複数コマンドを実行する
        Args:
            commands (list[Command]): Commandのサブクラスの配列
        """
        for cmd in commands:
            self.execute(cmd)

    def execute(self, cmd):
        """コマンドを実行する
        Args:
            cmd (Command): Commandクラス
        """
    
        if isinstance(cmd, Rotate):
            self.servo.rotate(vertical=cmd.vertical, horizontal=cmd.horizontal)
        else:
            self.servo.to_default()
