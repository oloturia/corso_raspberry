#!/usr/bin/env python3

import signal
import time
import grovepi
import grove_rgb_lcd
import tkinter as tk
from tkinter import ttk

led = 4
state = False

seconds_elapsed = 0

def deactivate_led_display():
    grovepi.digitalWrite(led,0)
    grove_rgb_lcd.setText("")
    grove_rgb_lcd.setRGB(0,0,0)
    quit()    

def exit_handler(signum, frame):
    grovepi.digitalWrite(led,0)
    deactivate_led_display()
    
def led_toggle():
    global state
    global led
    state = not state
    grovepi.digitalWrite(led,state)
    return

def time_count():
    global seconds_elapsed
    disp = str(seconds_elapsed)
    seconds_elapsed += 1
    clock.config(text=disp)
    clock.after(1000,time_count)
    
def write_to_display():
    grove_rgb_lcd.setText(display_text.get("1.0","2.15"))
    display_text.text=""
    return

signal.signal(signal.SIGINT, exit_handler)

if __name__ == "__main__":
    grovepi.pinMode(led,"OUTPUT")
    grove_rgb_lcd.setRGB(200,125,125)

    root = tk.Tk()
    root.title("LED Controller")
    root.geometry("400x200")

    led_button = ttk.Button(root,text="LED",command=led_toggle)
    clock = ttk.Label(root,background='green')
    display_text = tk.Text(root, height=2, width=16)
    write_disp = ttk.Button(root,text="WRITE",command=write_to_display)
    quit_button = ttk.Button(root,text="Quit",command=lambda: root.quit())

    led_button.pack(side="top")
    clock.pack(anchor="n")
    display_text.pack(anchor="center")
    write_disp.pack(anchor="center")
    quit_button.pack(side="bottom")
    time_count()

    root.mainloop() 
    deactivate_led_display()


