#!coding=utf-8

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
from cowpy import cow

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        obj = urlparse(self.path)    
        txt = obj.ip
        with open('./ip.txt', 'w') as fh:
            txt = fh.write(txt)
        
        message = cow.Cowacter().milk(self.path)
        self.wfile.write(message.encode())
        return
