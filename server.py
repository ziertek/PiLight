from flask import flask, render_template

app = Flask(__name__)

@app.route("/")
def controller():
    return render_template('controller.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')