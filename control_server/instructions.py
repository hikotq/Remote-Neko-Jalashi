#-*-coding: utf-8-*-

def deg_to_pulse(deg):
    return (deg + 90) / 180 * 450 + 150

class Instruction(object):
    """
    Controllerクラスに与える各制御命令クラスの基底クラス
    各制御命令クラスはこのクラスを継承する
    """
    
class Rotate(Instruction):
    """
    回転を行う命令
    """
    def __init__(self, vertical=None, horizon=None, deg=None):
        self.vertical = None
        self.horizon = None
        if vertical is not None:
            self.vertical = deg_to_pulse(vertical) if deg else vertical
        if horizon is not None:
            self.horizon = deg_to_pulse(horizon) if deg else horizon

class Default(Instruction):
    """
    横軸方向への制御を行う命令
    """
