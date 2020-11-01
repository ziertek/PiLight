#!/usr/bin/env python

import colorsys
import time
import math
import os
from flask import Flask, render_template, request
from lib.phat_wrapper import PhatWrapper

hat = PhatWrapper()

app = Flask(__name__)

@app.route("/")
def controller():
    return render_template('controller.html')

# Colour routes, look at making them simply all the same API call with varriable instead
@app.route('/api/colour/Green')
def Green():
    hat.setAll(0,255,0)
    return ("nothing")

@app.route('/api/colour/Red')
def Red():
    hat.setAll(255,0,0)
    return ("nothing")

@app.route('/api/colour/Yellow')
def Yellow():
    hat.setAll(255,255,0)
    return ("nothing")

@app.route('/api/colour/Blue')
def Blue():
    hat.setAll(0,0,255)
    return ("nothing")

@app.route('/api/colour/Pink')
def Pink():
    hat.setAll(255,0,255)
    return ("nothing")

@app.route('/api/colour/Teal')
def Teal():
    hat.setAll(0,255,255)
    return ("nothing")

@app.route('/api/colour/Rainbow')
def Rainbow():
    i = 0.0
    offset = 30
    while True:
            i = i + 0.3
            for y in range(4):
                    for x in range(8):
                            r = 0#x * 32
                            g = 0#y * 32
                            xy = x + y / 4
                            r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
                            g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
                            b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
                            r = max(0, min(255, r + offset))
                            g = max(0, min(255, g + offset))
                            b = max(0, min(255, b + offset))
                            hat.set_pixel(x,y,int(r),int(g),int(b))
            hat.show()
            time.sleep(0.01)
    return ("nothing")

@app.route('/api/colour/CustomColour',  methods=['POST'])
def CustomColour():
    red = request.form['Red']
    green = request.form['Green']
    blue = request.form['Blue']
    hat.setAll(red,green,blue)
    return render_template('controller.html')

@app.route('/api/colour/Blank')
def Blank():
    hat.clear()
    return ("nothing")

@app.route('/api/system/Update')
def Update():
    os.system("/opt/UpdateScript/Update.sh")
    return ("nothing")

@app.route('/api/system/Shutdown')
def Shutdown():
    os.system("shutdown +2 'Shutdown trigger via API... Shutting down in 2 minute'")
    return ("nothing")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')