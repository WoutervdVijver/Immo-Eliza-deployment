import pandas as pd
import numpy as np




# class ModelCreator:

#     def __init__(X_train, y_train):
#         self
    
#     def train():

#         linreg = LinearRegression()
#         linreg.fit(self.X_train, self.y_train)

#         return linreg


class ModelBuilder:

    def __init__(self, model):
        self.model = model

    def predict(self, X:dict):
        return np.round(np.exp(self.model.predict(pd.DataFrame(X))),2)

