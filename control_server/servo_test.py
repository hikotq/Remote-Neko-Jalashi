from controller import Controller
from commands import Rotate, Default
from servo import Servo

def main():
    servo = Servo()
    ctrl = Controller(servo)
    #縦方向の動作テストコマンド
    vertical_test_cmd = [\
                Default(),\
                Rotate(vertical=-90, deg=True),\
                Rotate(vertical=90, deg=True),\
                Default(),\
                Rotate(vertical=-90, deg=True),\
                Rotate(vertical=90, deg=True),\
                Default()\
            ]
    #横方向の動作テストコマンド
    horizon_test_cmd = [\
                Default(),\
                Rotate(horizon=-90, deg=True),\
                Rotate(horizon=90, deg=True),\
                Default(),\
                Rotate(horizon=-90, deg=True),\
                Rotate(horizon=90, deg=True),\
                Default()\
            ]
    #縦と横の両方向を組み合わせた動作テストコマンド
    combine_test_cmd = [\
                Default(),\
                Rotate(vertical=-90, horizon=-90, deg=True),\
                Rotate(vertical=90, horizon=90, deg=True),\
                Default(),\
                Rotate(vertical=-90, horizon=-90, deg=True),\
                Rotate(vertical=90, horizon=90, deg=True),\
                Default()\
            ]
    #実行
    ctrl.execute_commands(vertical_test_cmd)
    ctrl.execute_commands(horizon_test_cmd)
    ctrl.execute_commands(combine_test_cmd)

if __name__=='__main__':
    main()
