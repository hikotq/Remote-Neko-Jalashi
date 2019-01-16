#-*-coding: utf-8-*-

def deg_to_pulse(deg):
    """角度表記を信号幅に変換する
    Args:
        deg (int): サーボの角度
        
    Returns:
        int: 角度に対応する信号幅
    """
    return int(float(deg - 150) / 450 * 180 - 90)

class Command(object):
    """
    Controllerクラスに与える各制御命令クラスの基底クラス
    各制御命令クラスはこのクラスを継承する
    """
    
class Rotate(Command):
    """
    回転を行う命令
    """
    def __init__(self, vertical=None, horizontal=None, deg=None):
        self.vertical = None
        self.horizontal = None
        if vertical is not None:
            self.vertical = deg_to_pulse(vertical) if deg else vertical
        if horizontal is not None:
            self.horizontal = deg_to_pulse(horizontal) if deg else horizontal

class Default(Command):
    """
    横軸方向への制御を行う命令
    """
