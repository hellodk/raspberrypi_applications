'''
Blinking LED using Pulse width modulation
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)

pwm = GPIO.PWM(21, 50)
pwm.start(0)

while True:
    for i in range(100):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.02)

    for i in range(100):
        pwm.ChangeDutyCycle(100-i)
        time.sleep(0.02)
