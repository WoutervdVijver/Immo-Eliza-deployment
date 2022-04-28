from sklearn.linear_model import LinearRegression




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

    def predict(self, X):
        return self.model.predict(X)

