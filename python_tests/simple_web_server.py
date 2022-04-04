#!/usr/bin/env python3

import http.server
import socketserver

from urllib.parse import parse_qs
from urllib.parse import urlparse

import grovepi

led = 4
grovepi.pinMode(led,"OUTPUT")

class requestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path.startswith('/led'):
            query_components = parse_qs(urlparse(self.path).query)
            if 'status' in query_components:
                if query_components['status'] == ['on']:
                    grovepi.digitalWrite(led,1)
                else:
                    grovepi.digitalWrite(led,0)
        with open('webpage.html','r') as led_page:
            self.wfile.write(bytes(led_page.read(), "utf8"))
        return

led_server = socketserver.TCPServer(('',8000), requestHandler)

try:
    led_server.serve_forever()
except KeyboardInterrupt:
    print("Shutting down server...")
    grovepi.digitalWrite(led,0)
