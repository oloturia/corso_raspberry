#!/usr/bin/env python3

import grovepi
import grove_rgb_lcd 

button = 6
led = 4
grovepi.pinMode(led,"OUTPUT")
grovepi.pinMode(button,"INPUT")
grove_rgb_lcd.setRGB(200,125,125)
grove_rgb_lcd.setText("0")

count = 0

while True:
	try:
		read_button = grovepi.digitalRead(button)
		if read_button == 1:
			grovepi.digitalWrite(led,1)
			count +=1
			grove_rgb_lcd.setText(str(count))
		else:
			grovepi.digitalWrite(led,0)
			
	
	except KeyboardInterrupt:
		grovepi.digitalWrite(led,0)
		break
	except IOError:
		print("error")
		break
