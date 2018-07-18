from flask import Flask, render_template, request
from data04 import areaData, salaryData, position_dict, get_result
from first_db import query_db

app = Flask(__name__)
url = position_dict[request.args.get('position_name')]
salary = salaryData(url)
name, num = areaData(url)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():

    return render_template('index.html', salary = salary, name = name, num = num)

if __name__ == '__main__':
    app.run(debug = True)
