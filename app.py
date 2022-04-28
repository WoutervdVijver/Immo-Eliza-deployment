from flask import Flask, request, jsonify
import joblib
from markupsafe import escape

from model.model import ModelBuilder

my_model = ModelBuilder(joblib.load('first_model'))

app = Flask(__name__)



@app.route('/', methods=['GET'])
def hello():
    return 'Welcome'




@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        return 'POST'
    if request.method == 'GET':
        return 'GET'





db_users = {
    "John" : "Miami",
    "David" : "Miami",
    "Jane" : "London",
    "Gabriella" : "Paris",
    "Tanaka" : "Tokyo"
}

@app.route('/search', methods=['GET'])
def search():
    args = request.args
    name = args.get('name')
    location = args.get('location')

    # result = db_users
    if None not in (name, location):
        result = {key: value for key, value in db_users.items() if key == name and value == location}
    elif name is not None:
        result = {key: value for key, value in db_users.items() if key == name}
    elif location is not None:
        result = {key: value for key, value in db_users.items() if value == location}

    return result




if __name__ == '__main__':
   app.run(port=4000)