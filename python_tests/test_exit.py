#!/usr/bin/python3
from time import sleep
print("Press Ctrl+C to exit")
while True:
	try:
		sleep(0.5)

	except KeyboardInterrupt as e:
		print(str(e))
		print("Exiting...")
		break

