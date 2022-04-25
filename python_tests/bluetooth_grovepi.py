#!/usr/bin/env python3

import grovepi
import serial

ser = serial.Serial('/dev/rfcomm0',9600) 
led = 4
ultrasonic_ranger = 6

grovepi.pinMode(led,"OUTPUT")

if __name__ == "__main__":
	while True:
		result = ser.read()
		print(result)
		if result == b'1':
				grovepi.digitalWrite(led,1)
		elif result == b'0':
                		grovepi.digitalWrite(led,0)
		else:
		    answer = str(grovepi.ultrasonicRead(ultrasonic_ranger))
		    byte_answer = bytes( str(answer), 'ascii')
		    ser.write(byte_answer)
