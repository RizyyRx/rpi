import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

channels=[12,13,19]
for c in channels:
    GPIO.setup(c,GPIO.OUT)

try:
    while True:
        try:
            num = int(input("Enter number between 0 to 7:"))
            if num < 0 or num > 7:
                print("Enter number in correct range....")
                continue
            print("you entered "+str(num))
            
            rgb = format(num,'03b')
            
            for i,c in enumerate(channels):
                print(i,c,rgb[i])
                GPIO.output(c,not bool(int(rgb[i])))

        except ValueError:
            print("Invalid input, try again....")
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Stopping.....")
