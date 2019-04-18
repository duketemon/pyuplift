import numpy as np
from sklearn.linear_model import LinearRegression
from pyuplift import BaseModel


class Econometric(BaseModel):
    """Econometric approach.
    Building two independent models and predicting effect as difference.
    Method description available in the article
    "A Literature Survey and Experimental Evaluation of the State-of-the-Art in Uplift Modeling:
    A Stepping Stone Toward the Development of Prescriptive Analytics"
    by Floris Devriendt, Darie Moldovan, and Wouter Verbeke
    """
    def __init__(self, model=LinearRegression()):
        self.model = model

    def fit(self, X, y, t):
        """The method description you can find in the base class"""
        x_train = self.__get_matrix(X, t)
        self.model.fit(x_train, y)

    def predict(self, X, t=None):
        """The method description you can find in the base class"""
        x_test = self.__get_matrix(X, np.array(X.shape[0] * [0]))
        v0 = self.model.predict(x_test)
        x_test = self.__get_matrix(X, np.array(X.shape[0] * [1]))
        v1 = self.model.predict(x_test)
        return v1 - v0

    def __get_matrix(self, X, t):
        """Create X|T|X*T matrix"""
        x_t = np.append(X, t.reshape((-1, 1)), axis=1)
        xt = X * t.reshape((-1, 1))
        return np.append(x_t, xt, axis=1)
