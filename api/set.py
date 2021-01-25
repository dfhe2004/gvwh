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
        ip = obj.get('ip',None)
        if bool(ip):
            with open('./ip.txt', 'w') as fh:
                txt = file.write(ip)
        else:
            txt = 'invalid ip'
        message = cow.Cowacter().milk(txt)
        self.wfile.write(message.encode())
        return
