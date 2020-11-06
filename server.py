#!/usr/bin/env python

import colorsys
import time
import math
import os
from flask import Flask, render_template, request
from lib.phat_wrapper import PhatWrapper

gStatus = "Initialized"

hat = PhatWrapper()
hat.setAll(255,255,255)

app = Flask(__name__)

@app.route("/")
def controller():
    return render_template('controller.html')

# Colour routes, look at making them simply all the same API call with varriable instead
@app.route('/api/colour/Green')
def Green():
    global gStatus
    gStatus = "Green"
    hat.setAll(0,255,0)
    return 'OK'

@app.route('/api/colour/Red')
def Red():
    global gStatus
    gStatus = "Red"
    hat.setAll(255,0,0)
    return 'OK'

@app.route('/api/colour/Yellow')
def Yellow():
    global gStatus
    gStatus = "Yellow"
    hat.setAll(255,255,0)
    return 'OK'

@app.route('/api/colour/Blue')
def Blue():
    global gStatus
    gStatus = "Blue"
    hat.setAll(0,0,255)
    return 'OK'

@app.route('/api/colour/Pink')
def Pink():
    global gStatus
    gStatus = "Pink"
    hat.setAll(255,0,255)
    return 'OK'

@app.route('/api/colour/Teal')
def Teal():
    global gStatus
    gStatus = "Teal"
    hat.setAll(0,255,255)
    return 'OK'

@app.route('/api/colour/Rainbow')
def Rainbow():
    global gStatus
    gStatus = "Rainbow"
    i = 0.0
    offset = 30
    while gStatus == "Rainbow":
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
                            hat.setPixel(x,y,int(r),int(g),int(b))
            hat.show()
            time.sleep(0.01)
    return 'OK'

@app.route('/api/colour/CustomColour',  methods=['POST'])
def CustomColour():
    global gStatus
    gStatus = "Custom"
    red = request.form['Red']
    green = request.form['Green']
    blue = request.form['Blue']
    print(red,green,blue)
    #hat.setAll(red,green,blue)
    return 'OK'

@app.route('/api/colour/Blank')
def Blank():
    global gStatus
    gStatus = "Blank"
    hat.clear()
    return 'OK'

# System routes
@app.route('/api/system/UpdatePi')
def UpdatePi():
    global gStatus
    gStatus = "Update Pi"
    hat.clear()
    os.system("Update/UpdatePi.sh")
    return 'OK'

@app.route('/api/system/Shutdown')
def Shutdown():
    global gStatus
    gStatus = "Shutdown"
    hat.clear()
    os.system("shutdown now 'Shutdown trigger via API'")
    return 'OK'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')