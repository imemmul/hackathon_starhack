from flask import Flask, jsonify, request
import pandas as pd

data_car_dict = {}
data_stores = [{'name':'White Bakery', 'duration': 5, 'price':30, 'latitude':37.0202875421039, 'longtitude':30.5981990104282},
            {'name':'McDonalds', 'duration':15, 'price':23, 'latitude':36.886827290282, 'longtitude':30.7025303036082},
            {'name': 'Beach Bar', 'duration':45, 'price':55, 'latitude':36.6137941584317, 'longtitude':30.5610624029243},
            {'name':'Coffee Shop', 'duration':10, 'price':5, 'latitude':36.9964701515979, 'longtitude':30.8528972730965},
            {'name':'Burger King', 'duration':17, 'price':21, 'latitude':36.8867220621227, 'longtitude':30.8187125270902},
            {'name':"Maria's Coffee", 'duration':10, 'price':18, 'latitude':36.8513376776303,'longtitude':30.8505665675635}]

def read_car_csv():    
    data_car_dict = pd.read_csv('data_car.csv').to_dict()
    return data_car_dict


app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to our app"

@app.route('/takeorder', methods = ['POST'])
def post():
    if request.method == 'POST':
        return jsonify(read_car_csv())

@app.route('/stores', methods= ['POST'])
def post_store():
    if request.method == 'POST':
        return jsonify(data_stores)

def main():
    app.run()

if __name__ == "__main__":
    main()