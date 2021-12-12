from flask import Flask, jsonify, request
import csv

def read_car_csv():    
    with open("data_car.csv", "r") as file:
        data = file.read()
    rows = data.split("\n")
    data_car_dict = {}
    for row in rows:
        info = row.split(",")
    order_id = int(info[0])
    order_type = info[1]
    latitude = float(info[2])
    longtitude = float(info[3])
    data_car_dict[order_id] = {"order_type":order_type,
                                "latitude":latitude,
                                "longtitude":longtitude}
    return data_car_dict


app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to our app"

@app.route('/takeorder', methods = ['POST'])
def post():
    if request.method == 'POST':
        #data = request.form[example_json]
        return jsonify(read_car_csv())

# @app.route('/stores', methods= ['POST'])
# def post_store():
#     if request.method == 'POST':
#         return jsonify(data_stores)


if __name__ == "__main__":
    #read_data(data_stores)
    #read_data(data_json)
    app.run()