#!/usr/bin/env python3

import RPi.GPIO as GPIO
import serial

ser = serial.Serial('/dev/rfcomm0',9600) 

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(7,GPIO.OUT)
	
	no_answer = 0	

	while True:
		result = ser.read()
		print(result)
		if result == b'1':
				GPIO.output(7,1)
		elif result == b'0':
				GPIO.output(7,0)
		byte_answer = bytes( str(no_answer), 'ascii')
		ser.write(byte_answer)
		no_answer += 1
