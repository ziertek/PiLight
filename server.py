from flask import Flask, render_template
from unicorn_wrapper import UnicornWrapper

unicorn = UnicornWrapper()

app = Flask(__name__)

def setRGB(R,G,B):
    unicorn.setAll(R,G,B)
    return

@app.route("/")
def controller():
    return render_template('controller.html')

# Colour routes
@app.route('/api/Green')
def Green():
    setRGB(0,255,0)
    print ("Green")
    return ("nothing")

@app.route('/api/Red')
def Red():
    setRGB(255,0,0)
    print ("Red")
    return ("nothing")

@app.route('/api/Yellow')
def Yellow():
    setRGB(255,255,0)
    print ("Yellow")
    return ("nothing")

@app.route('/api/Blue')
def Blue():
    setRGB(0,0,255)
    print ("Blue")
    return ("nothing")

@app.route('/api/Pink')
def Pink():
    setRGB(255,0,255)
    print ("Red")
    return ("nothing")

@app.route('/api/Teal')
def Teal():
    setRGB(0,255,255)
    print ("Teal")
    return ("nothing")

@app.route('/api/CustomColour')
def CustomColour():
    print ("Custom")
    return ("nothing")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')