import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(ledpin1, GPIO.OUT)
