import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
channel=27

GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		if(GPIO.input(channel) == GPIO.HIGH):
			print("bam!!!  " + str(time.time()))
			time.sleep(0.5)
except KeyboardInterrupt:
	print("zzzzz")
	GPIO.cleanup()
