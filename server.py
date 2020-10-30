#!/usr/bin/env python

from flask import Flask, render_template
from lib.phat_wrapper import PhatWrapper

hat = PhatWrapper()

app = Flask(__name__)

@app.route("/")
def controller():
    return render_template('controller.html')

# Colour routes, look at making them simply all the same API call with varriable instead
@app.route('/api/Green')
def Green():
    hat.setAll(0,255,0)
    print ("Green")
    return ("nothing")

@app.route('/api/Red')
def Red():
    hat.setAll(255,0,0)
    print ("Red")
    return ("nothing")

@app.route('/api/Yellow')
def Yellow():
    hat.setAll(255,255,0)
    print ("Yellow")
    return ("nothing")

@app.route('/api/Blue')
def Blue():
    hat.setAll(0,0,255)
    print ("Blue")
    return ("nothing")

@app.route('/api/Pink')
def Pink():
    hat.setAll(255,0,255)
    print ("Pink")
    return ("nothing")

@app.route('/api/Teal')
def Teal():
    hat.setAll(0,255,255)
    print ("Teal")
    return ("nothing")

@app.route('/api/CustomColour')
def CustomColour():
    print ("Custom")
    return ("nothing")

@app.route('/api/Blank')
def Blank():
    hat.clear()
    print ("Blank")
    return ("nothing")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')