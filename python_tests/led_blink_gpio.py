#!/usr/bin/env python3

import RPi.GPIO as GPIO
import signal
import time

#Facciamo lampeggiare un LED, ma usciamo con stile

def exit_handler(signum, frame):
	GPIO.cleanup()
	exit()

signal.signal(signal.SIGINT, exit_handler)

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(7,GPIO.OUT)
	
	while True:
		GPIO.output(7,1)
		time.sleep(1)
		GPIO.output(7,0)
		time.sleep(1)

