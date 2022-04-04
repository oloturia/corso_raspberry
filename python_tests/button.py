#!/usr/bin/env python3

import grovepi


button = 6
led = 3
grovepi.pinMode(led,"OUTPUT")
grovepi.pinMode(button,"INPUT")

while True:
	try:
		read_button = grovepi.digitalRead(button)
		if read_button == 1:
			grovepi.digitalWrite(led,1)
		else:
			grovepi.digitalWrite(led,0)
	except KeyboardInterrupt:
		grovepi.digitalWrite(led,0)
		break
	except IOError:
		print("error")
		break
