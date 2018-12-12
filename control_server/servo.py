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

    def horizon(self, pulse):
        """
        横軸の位置を変更する
        Parameters
        ----------
        pulse: int
            PCA9685に送る信号幅
        """
        pulse = Servo.pulse_correction(pulse)
        self.pwm.set_pwm(HORIZON, 0, pulse)
        self.sleep()
        
    def vertical(self, pulse):
        """
        縦軸の位置を変更する
        Parameters
        ----------
        pulse: int
            PCA9685に送る信号幅
        """
        pulse = Servo.pulse_correction(pulse)
        self.pwm.set_pwm(VERTICAL, 0, pulse)
        self.sleep()

    def test(self):
        """
        動作テスト用メソッド
        """
        self.to_default()
        self.horizon_test()
        self.to_default()
        self.vertical_test()
        self.to_default()
        self.vertical_horizon_test()
        self.to_default()
        
    def horizon_test(self):
        """
        垂直方向の動作テストを行う

        Parameters
        ----------
        pwm: PCA9685
            PCA9685を操作するクラスのインスタンス
        """
        logging.info("vertical_test: started")
        for _ in range(2):
            self.pwm.set_pwm(HORIZON, 0, SERVO_MIN)
            self.sleep()
            self.pwm.set_pwm(HORIZON, 0, SERVO_MAX)
            self.sleep()
        logging.info("vertical_test: done")
            
    def vertical_test(self):
        """
        垂直方向の動作テストを行う

        Parameters
        ----------
        pwm: PCA9685
            PCA9685を操作するクラスのインスタンス
        """
        logging.info("vertical_test: started")
        for _ in range(2):
            self.pwm.set_pwm(VERTICAL, 0, SERVO_MIN)
            self.sleep()
            self.pwm.set_pwm(VERTICAL, 0, SERVO_MAX)
            self.sleep()
        logging.info("vertical_test: done")


    def vertical_horizon_test(self):
        """
        垂直, 水平合わせた動作テストを行う

        Parameters
        ----------
        pwm: PCA9685
            PCA9685を操作するクラスのインスタンス
        """

        logging.info("vertical_horizon_test: started")
        for _ in range(2):
            self.pwm.set_pwm(VERTICAL, 0, SERVO_MIN)
            self.pwm.set_pwm(HORIZON, 0, SERVO_MIN)
            self.sleep()
            self.pwm.set_pwm(VERTICAL, 0, SERVO_MAX)
            self.pwm.set_pwm(HORIZON, 0, SERVO_MAX)
            self.sleep()
            
        logging.info("vertical_horizon_test: done")
