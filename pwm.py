import RPi.GPIO as GPIO

channel = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, 2) #channel, frequency
p.start(100)

try:
    while True:
        try:
            d = input("Enter duty cycle:")
            f = input("Enter frequency:")

            if (d == 'q' or f == 'q'):
                break
            
            p.ChangeDutyCycle(int(d))
            p.ChangeFrequency(int(f))
        except ValueError as e:
            pass
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
