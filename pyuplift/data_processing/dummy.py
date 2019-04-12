import numpy as np
from sklearn.linear_model import LinearRegression
from pyuplift import BaseModel


class Dummy(BaseModel):
    """Dummy (or treatment as variable) approach.
    Method description available in the article
    "A Literature Survey and Experimental Evaluation of the State-of-the-Art in Uplift Modeling:
    A Stepping Stone Toward the Development of Prescriptive Analytics"
    by Floris Devriendt, Darie Moldovan, and Wouter Verbeke
    """
    def __init__(self, model=LinearRegression()):
        self.model = model

    def fit(self, X, y, t):
        """The method description you can find in the base class"""
        x_train = np.append(X, t.reshape((-1, 1)), axis=1)
        self.model.fit(x_train, y)
        return self

    def predict(self, X, t=None):
        """The method description you can find in the base class"""
        col = np.array(X.shape[0] * [0])
        x_test = np.append(X, col.reshape((-1, 1)), axis=1)
        # All treatment values == 0
        s0 = self.model.predict(x_test)
        x_test[:, -1] = 1
        # All treatment values == 1
        s1 = self.model.predict(x_test)
        return s1 - s0
