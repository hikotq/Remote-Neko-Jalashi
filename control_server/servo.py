#! /usr/bin/python
#-*-coding: utf-8-*-

import time
import Adafruit_PCA9685
import logging
logging.basicConfig(filename='servo.log', level=logging.DEBUG)

SERVO_MIN = 150    # -90度
SERVO_MAX = 600    # +90度

HORIZON = 8
VERTICAL = 7

class Servo(object):
    def __init__(self):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)
        self.pwm = pwm
        self.sleep_sec = 1.0

    def to_default(self):
        self.pwm.set_pwm(VERTICAL, 0, 375)
        self.pwm.set_pwm(HORIZON, 0, 375)
        self.sleep()

    @classmethod
    def pulse_correction(cls, pulse):
        """
        pulseの値をSERVO_MINからSERVO_MAXの範囲内に補正する
        Parameters
        ----------
        pulse: int
            補正を行う信号幅の値
        """
        if pulse > SERVO_MAX:
            return SERVO_MAX
        elif pulse < SERVO_MIN:
            return SERVO_MIN
        else:
            return pulse
        
    def sleep(self):
        time.sleep(self.sleep_sec)

    def rotate(self, vertical=None, horizon=None):
        """
        サーボを回転させる
        Parameters
        ----------
        vertical: int
            サーボの縦軸方向の回転制御用信号
        horizon: int
            サーボの横軸方向の回転制御用信号
        """
        if vertical is not None:
            vertical = Servo.pulse_correction(vertical)
            self.pwm.set_pwm(VERTICAL, 0, pulse)
        if horizon is not None:
            horizon = Servo.pulse_correction(horizon)
            self.pwm.set_pwm(HORIZON, 0, pulse)
        self.sleep()
