#! /usr/bin/python
#-*-coding: utf-8-*-

import time
import Adafruit_PCA9685

SERVO_MIN = 150    # -90度
SERVO_MAX = 600    # +90度

HORIZON = 8
VERTICAL = 7


    #0.5秒おきに左右90度に動く
    print('Moving servo on channel 0, press Ctrl-C to quit...')
    while True:
        pwm.set_pwm(7, 0, servo_min)
        time.sleep(0.5)
        pwm.set_pwm(7, 0, servo_max)
        time.sleep(0.5)
