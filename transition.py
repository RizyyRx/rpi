import RPi.GPIO as GPIO
from time import sleep

channel = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.OUT)

p=GPIO.PWM(channel,60)
print("starting pwm...")
p.start(0)
a=0
try:
    while True:
        # a=0
        for dc in range(0,101,1): 
            p.ChangeDutyCycle(dc)
            sleep(0.01)
            # print(a)
            # a+=1
        for dc in range(100,-1,-1): 
            p.ChangeDutyCycle(dc)
            sleep(0.01)
            # print(a)
            # a+=1
except KeyboardInterrupt:
    p.stop()
    print("Exitting....")
    GPIO.cleanup()