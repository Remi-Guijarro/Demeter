import gpiozero
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

state = GPIO.input(7)

print(state)

if state :
	GPIO.output(7, GPIO.LOW)
else :
	GPIO.output(7, GPIO.HIGH)
