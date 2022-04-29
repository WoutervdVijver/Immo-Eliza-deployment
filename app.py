from flask import Flask, redirect, request, render_template, url_for, jsonify
import joblib

from model.model import ModelBuilder
from preprocessing.cleaning_data import preprocess

app = Flask(__name__)

my_model = ModelBuilder(joblib.load('first_model'))


@app.route('/')
def hello():
    return 'Welcome'



@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            data = request.form
            data = preprocess(data)
            prediction = my_model.predict(data)
            return render_template('prediction.html', prediction = prediction)
        except:
            return 'Something went wrong'
    else:
        return render_template('predict.html')

@app.route('/prediction')
def prediction():
    pass


if __name__ == '__main__':
   app.run(debug=True, port=4000)