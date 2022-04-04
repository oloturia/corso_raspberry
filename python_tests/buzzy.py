#!/usr/bin/env python3

import grovepi
import time

buzzer = 6
potentiometer = 0
grovepi.pinMode(buzzer,"OUTPUT")
grovepi.pinMode(potentiometer,"INPUT")

while True:
	try:
		note = int((grovepi.analogRead(potentiometer)/1023)*255)
		grovepi.analogWrite(buzzer,note)
		time.sleep(1)
	except KeyboardInterrupt:
		grovepi.analogWrite(buzzer,0)
		break
	except IOError:
		print("error")
		break
