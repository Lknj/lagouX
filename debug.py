from flask import Flask, render_template, request
from data import allData, position_dict, get_result
from first_db import query_db

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@app.route('/next', methods = ['GET', 'POST'])
def show_data():
    p_name = request.args.get('position_name')
    dictA = position_dict()
    url = dictA[str(p_name)]
    data_position_name = '%' + p_name + '%'
    salary, education, name, num, experience_name, experience_num = allData(str(data_position_name), url)

    if request.args.get('query') == "查询":
        return render_template('query.html', salary = salary, education = education, name = name, num = num, experience_name = experience_name, experience_num = experience_num)

if __name__ == '__main__':
    app.run(debug = True)
