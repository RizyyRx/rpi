import RPi.GPIO as GPIO

channel = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, 1000) #channel, frequency
p.start(100)

try:
    while True:
        try:
            b = input("Change brightness:")

            if (b == 'q'):
                break
            
            p.ChangeDutyCycle(int(b))
        except ValueError as e:
            pass
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
