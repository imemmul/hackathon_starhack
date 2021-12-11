from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

data_json = dict()
reader = csv.DictReader(open('data.csv'))
for row in reader:
    data_json.update(row)

@app.route('/')
def index():
    return "Welcome to our app"

@app.route('/takeorder', methods = ['POST'])
def post():
    if request.method == 'POST':
        #data = request.form[example_json]
        return jsonify(data_json)


if __name__ == "__main__":
    app.run()