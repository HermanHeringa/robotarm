import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
for i in [2, 3, 14, 15, 17, 18, 27, 22, 23, 24, 25]:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.LOW)
time.sleep(2)
GPIO.output(23, GPIO.HIGH)
time.sleep(1)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.HIGH)
time.sleep(1)
GPIO.output(24, GPIO.LOW)
GPIO.output(22, GPIO.HIGH)
time.sleep(1)
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.HIGH)
time.sleep(1)
GPIO.output(27, GPIO.LOW)
GPIO.output(18, GPIO.HIGH)
time.sleep(1)
GPIO.output(18, GPIO.LOW)
GPIO.output(17, GPIO.HIGH)
time.sleep(1)
GPIO.output(17, GPIO.LOW)
GPIO.output(15, GPIO.HIGH)
time.sleep(1)
GPIO.output(15, GPIO.LOW)
GPIO.output(14, GPIO.HIGH)
time.sleep(1)
GPIO.output(14, GPIO.LOW)
GPIO.output(3, GPIO.HIGH)
time.sleep(1)
GPIO.output(3, GPIO.LOW)
GPIO.output(2, GPIO.HIGH)
time.sleep(1)
GPIO.output(2, GPIO.LOW)
GPIO.output(25, GPIO.HIGH)
time.sleep(1)
GPIO.output(25, GPIO.LOW)
