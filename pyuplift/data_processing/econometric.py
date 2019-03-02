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
        x_t = np.append(X, t.reshape((-1, 1)), axis=1)
        xt = X * t.reshape((-1, 1))
        x_train = np.append(x_t, xt, axis=1)
        self.model.fit(x_train, y)

    def predict(self, X, t=None):
        """The method description you can find in the base class"""
        x_test = self.__get_test_X(X, 0)
        s0 = self.model.predict(x_test)
        x_test = self.__get_test_X(X, 1)
        s1 = self.model.predict(x_test)
        return s1 - s0

    def __get_test_X(self, X, value):
        """Create X|T|X*T matrix"""
        t = np.array(X.shape[0] * [value])
        x_t = np.append(X, t.reshape((-1, 1)), axis=1)
        xt = X * t.reshape((-1, 1))
        return np.append(x_t, xt, axis=1)
