from flask import Flask, redirect, request, render_template, url_for, jsonify
import joblib
import os

from model.model import ModelBuilder, ModelCreator
from preprocessing.cleaning_data import Preprocess

app = Flask(__name__)

my_model = ModelBuilder(joblib.load("./model/house_model"))


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Function that creates the homepage and redirect if one of the buttons on the webpage are pushed
    """
    if request.method == "GET":
        return render_template("index.html")
    else:
        if request.form["button"] == "update":
            return redirect("/update")
        else:
            return redirect("/predict")


@app.route("/predict", methods=["POST", "GET"])
def predict():
    """
    Function that renders the webform to accept the data of one house.
    When the data has been entered it preprocesses the data and makes a price prediction.
    """
    if request.method == "POST":
        try:
            data = request.form
            prepro = Preprocess(data)
            prepro.clean_all()
            prediction = my_model.predict(prepro.dict)
            return render_template("prediction.html", prediction=prediction)
        except:
            return render_template("predicterror.html")
    else:
        return render_template("predict.html")


@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    """
    Function that creates a website to display the prediction.
    """
    if request.method == "GET":
        return render_template("prediction.html", prediction=[7])
    else:
        if request.form["button"] == "predict":
            return redirect("/predict")
        else:
            return redirect("/")


@app.route("/predicterror", methods=["GET", "POST"])
def error():
    """
    Function that displays a website with an error message when the form has not been filled in correctly
    """
    if request.method == "GET":
        return render_template("predicterror.html")
    else:
        return redirect("/predict")


@app.route("/update", methods=["GET", "POST"])
def update():
    """
    Function creates website where the model can be retrained
    """
    if request.method == "GET":
        return render_template("update.html")
    else:
        if request.form["button"] == "form":
            return render_template("predict.html")
        else:
            creator = ModelCreator()
            creator.train()
            return redirect("/index")


if __name__ == "__main__":
    # You want to put the value of the env variable PORT if it exist (some services only open specifiques ports)
    port = int(os.environ.get("PORT", 5000))
    # Threaded option to enable multiple instances for
    # multiple user access support
    # You will also define the host to "0.0.0.0" because localhost will only be reachable from inside de server.
    app.run(host="0.0.0.0", threaded=True, port=port)
