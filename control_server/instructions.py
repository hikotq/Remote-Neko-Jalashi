#-*-coding: utf-8-*-

class Instruction(object):
    """
    Controllerクラスに与える各制御命令クラスの基底クラス
    各制御命令クラスはこのクラスを継承する
    """
    
class Horizon(Instruction):
    """
    縦軸方向への制御を行う命令
    """
    def __init__(self, pulse):
        self.pulse = pulse
        
class Vertical(Instruction):
    """
    横軸方向への制御を行う命令
    """
    def __init__(self, pulse):
        self.pulse = pulse

class Default(Instruction):
    """
    横軸方向への制御を行う命令
    """
