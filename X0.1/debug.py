from flask import Flask, render_template
from data03 import areaData
from data import xzData
app = Flask(__name__)
xz = xzData()
name, num = areaData()

@app.route('/')
def hello_world():
    return render_template('index.html', xz = xz, name = name, num = num)

if __name__ == '__main__':
    app.run(debug = True)
