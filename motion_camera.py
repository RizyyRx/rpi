import RPi.GPIO as GPIO
import time
import os
from ratelimit import limits
from uuid import uuid4
from threading import Thread
import requests

DEVICE_ID = "raspi_cam_1"
STORAGE_LOCATION = "motion_captures"

if not os.path.exists(STORAGE_LOCATION):
    os.mkdir(STORAGE_LOCATION)

GPIO.setmode(GPIO.BCM)
channel = 27 

GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def upload_picture(filename):
    name = filename.split("/")[-1]

    url = "http://172.30.0.60:5000/api/motion/capture"

    payload = {}
    files=[
    ('file',(name, open(filename,'rb'),'image/jpeg'))
    ]
    headers = {
    'X-Authorization': 'Bearer c528f646-6fdd-47c0-8d45-616a7de64e17',
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

@limits(calls=1, period=1)
def click_picture():
    print("taking pic..")
    uuid = str(uuid4())
    os.system('libcamera-still -o '+STORAGE_LOCATION+ "/" +uuid+'.jpg --timeout 1000 --verbose 0')
    print("done")
    t = Thread(target = upload_picture, args=(STORAGE_LOCATION+ "/" +uuid+'.jpg',))
    t.start()

try:
    while True:
        if GPIO.input(channel):
            try:
                print("motion detected")
                click_picture()
            except Exception as e:
                print(f"Error taking picture: {e}")
            time.sleep(1)
except KeyboardInterrupt:
	print("zzzzz")
	GPIO.cleanup()
