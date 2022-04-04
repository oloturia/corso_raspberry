#!/usr/bin/python3

import socket


UDP_IP = ""
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data,addr = sock.recvfrom(1024)
    if data == b"on":
        print("turn on")
    elif data == b"off":
        print("turn off")
    else:
        print("received message: %s" % data)


