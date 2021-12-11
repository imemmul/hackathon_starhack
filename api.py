from flask import Flask, jsonify, request
import csv

app = Flask(__name__)
data_json = [{'order_id': 1, 'order_type': 'food', 'latitude': 10, 'longtitude': 20}]
data_stores = [{'name':'Starbucks', 'latitude':30.5, 'longtitude':50.5, 'duration':0.5}, {'name':'Burger', 'latitude':20.5, 'longtitude':35.5, 'duration':35}]

def read_data(data):
    reader = csv.DictReader(open('data_stores.csv'))
    for row in reader:
        data.update(row)

@app.route('/')
def index():
    return "Welcome to our app"

@app.route('/takeorder', methods = ['POST'])
def post():
    if request.method == 'POST':
        #data = request.form[example_json]
        return jsonify(data_json)

@app.route('/stores', methods= ['POST'])
def post_store():
    if request.method == 'POST':
        return jsonify(data_stores)


if __name__ == "__main__":
    #read_data(data_stores)
    #read_data(data_json)
    app.run()