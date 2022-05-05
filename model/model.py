import joblib
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor


class ModelCreator:
    """
    Class that loads the dataset and retrains the house_model
    """

    def __init__(self):
        self.dataset = pd.read_csv("./data/house_data.csv")

    def train(self):
        """
        Function that retrains the model
        """
        X = self.dataset.drop(columns=["Price", "Price_log", "Unnamed: 0"])
        y = self.dataset["Price_log"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, train_size=0.8, random_state=76
        )
        grb = GradientBoostingRegressor(
            learning_rate=0.2,
        )
        grb.fit(X_train, y_train)
        joblib.dump(grb, "./model/house_model")


class ModelBuilder:
    """
    class that loads a model to predict the housing price
    """

    def __init__(self, model):
        self.model = model

    def predict(self, X: dict) -> float:
        """
        Function that takes in cleaned data form a single house and returns a prediction as float

        :param X: dict that represents data of a single house
        """
        return np.round(np.exp(self.model.predict(pd.DataFrame(X))), 2)
