#!coding=utf-8

from http.server import BaseHTTPRequestHandler
import os
from cowpy import cow

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        if not os.path.exists('./ip.txt'):         
            txt = 'missing'
        else:
            with open('ip.txt'), 'r') as file:
                txt = file.read().strip()

        message = cow.Cowacter().milk(txt)
        self.wfile.write(message.encode())
        return
