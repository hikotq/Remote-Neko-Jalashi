
#-*-coding: utf-8-*-

import time
import Adafruit_PCA9685
import logging
logging.basicConfig(filename='servo.log', level=logging.DEBUG)

SERVO_MIN = 150    # -90度
SERVO_MAX = 600    # +90度

HORIZONTAL = 8
VERTICAL = 7

class Servo(object):
    """サーボと通信を行うモジュール
    """
    
    def __init__(self):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)
        self.pwm = pwm
        self.sleep_sec = 0.1

    def reset(cls):
        Adafruit_PCA9685.software_reset()

    def to_default(self):
        """サーボ位置をデフォルトにする
        """
        self.pwm.set_pwm(VERTICAL, 0, 375)
        self.pwm.set_pwm(HORIZONTAL, 0, 375)
        self.sleep()

    @classmethod
    def pulse_correction(cls, pulse):
        """pulseの値をSERVO_MINからSERVO_MAXの範囲内に補正する

        Args:
            pulse (int): 補正を行う信号幅の値
            
        Returns:
            int: 補正後の信号幅
        """
        if pulse > SERVO_MAX:
            return SERVO_MAX
        elif pulse < SERVO_MIN:
            return SERVO_MIN
        else:
            return pulse
        
    def sleep(self):
        """self.sleep_sec秒スリープする
        """
        time.sleep(self.sleep_sec)

    def rotate(self, vertical=None, horizontal=None):
        """
        サーボを回転させる
        
        Args:
            vertical (int): サーボの縦軸方向の回転制御用信号
            horizontal (int): サーボの横軸方向の回転制御用信号
        """

        print("Rotate: horizontal = {}, vertical = {}".format(horizontal, vertical))
        if vertical is not None:
            pulse = Servo.pulse_correction(vertical)
            self.pwm.set_pwm(VERTICAL, 0, pulse)
        if horizontal is not None:
            pulse = Servo.pulse_correction(horizontal)
            self.pwm.set_pwm(HORIZONTAL, 0, pulse)
        self.sleep()
