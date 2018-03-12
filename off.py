import RPi.GPIO as GPIO
import time
import os

#setup GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(13)
	#when input becomes low (button pushed) send shutdown command to OS
    if input_state == False:
        os.system("sudo shutdown now")
        time.sleep(0.2)
