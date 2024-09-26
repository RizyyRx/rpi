import RPi.GPIO as GPIO
from time import sleep

class RGB():

    #give channels to r,g,b
    def __init__(self,r,g,b):

        GPIO.setmode(GPIO.BCM)
        channels=[r,g,b]

        for c in channels:
            GPIO.setup(c,GPIO.OUT)

        # start pwm for r,g,b channels  
        self.r=GPIO.PWM(r,60)
        self.g=GPIO.PWM(g,60)
        self.b=GPIO.PWM(b,60)

        #start pwm for r,g,b
        self.r.start(0)
        self.g.start(0)
        self.b.start(0)

    #0-255 for rgb
    def setColour(self,r,g,b):

        #To create 255 values from 100
        r = (r/255) * 100 
        g = (g/255) * 100
        b = (b/255) * 100

        print(r,g,b)

        #change duty cycle
        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))

led=RGB(12,13,19)
led.setColour(255,100,51)
sleep(3)
GPIO.cleanup()