from flask import Flask, render_template
from data import xzData

app = Flask(__name__)
xz = xzData()
@app.route('/')
def hello_world():
    return render_template('index.html', xz = xz)

if __name__ == '__main__':
    app.run(debug = True)
