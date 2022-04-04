#!/usr/bin/env python3

import RPi.GPIO as GPIO
import signal
import time
import tkinter as tk

#Creiamo una finestra con Tkinter
#se si lancia il programma con DISPLAY=:0 la finestra verrà mostrata
#sul monitor HDMI

def exit_handler(signum, frame):
	GPIO.cleanup()
	exit()

signal.signal(signal.SIGINT, exit_handler)

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(7,GPIO.OUT)
	GPIO.output(7,1)
	
	root = tk.Tk()
	message = tk.Label(root, text="Hello World")
	message.pack()

	root.mainloop()	

	GPIO.cleanup()
