#!/usr/bin/python3

import socket

UDP_IP = "172.16.23.189"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    inp = input()
    sock.sendto(bytes(inp,'utf-8'),(UDP_IP,UDP_PORT))

