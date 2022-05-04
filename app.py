from flask import Flask, redirect, request, render_template, url_for, jsonify
import joblib

from model.model import ModelBuilder
from preprocessing.cleaning_data import Preprocess

app = Flask(__name__)

my_model = ModelBuilder(joblib.load('./model/best_model'))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return redirect('/predict')
    

@app.route('/book')
def hello():
    return render_template('book.html')



@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            data = request.form
            prepro = Preprocess(data)
            prepro.clean_all()
            prediction = my_model.predict(prepro.dict)
            return render_template('prediction.html', prediction = prediction)
        except:
            return render_template('predicterror.html')
    else:
        return render_template('predict.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'GET':
        return render_template('prediction.html', prediction=[7])
    else:
        if request.form['button'] == 'predict':
            return redirect('/predict')
        else:
            return redirect('/')

@app.route('/predicterror', methods=['GET', 'POST'])
def error():
    if request.method == 'GET':
        return render_template('predicterror.html')
    else:
        return redirect('/predict')


if __name__ == '__main__':
   app.run(debug=True, port=4000)