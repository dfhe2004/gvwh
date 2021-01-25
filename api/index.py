#!coding=utf-8

import os
from cowpy import cow


from sanic import Sanic
from sanic.response import json
app = Sanic()


@app.route('/')
@app.route('/<ip:ip>')
async def index(request, ip=""):
    if bool(ip):
        with open('./ip.txt', 'w') as fh:
            fh.write(ip)
        txt = 'save ip:%s'%ip    

    else:
        if not os.path.exists('./ip.txt'):         
            txt = 'missing'
        else:
            with open('./ip.txt', 'r') as file:
                txt = file.read().strip()
    
    txt = cow.Cowacter().milk(txt)
    return txt.encode()
