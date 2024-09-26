import RPi.GPIO as GPIO
from time import sleep

channel = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.OUT)

p=GPIO.PWM(channel,30)
print("starting pwm...")
p.start(50)
try:
    while True:
        print("glowing")
        sleep(1)
except KeyboardInterrupt:
    p.stop()
    print("Exitting....")
    GPIO.cleanup()