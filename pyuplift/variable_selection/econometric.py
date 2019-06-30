import numpy as np
from sklearn.linear_model import LinearRegression
from pyuplift import BaseModel


class Econometric(BaseModel):
    """The class which implements the econometric approach.

    +----------------+-----------------------------------------------------------------------------------+
    | **Parameters** | | **model : object, optional (default=sklearn.linear_model.LinearRegression)**    |
    |                | |   The regression model which will be used for predict uplift.                   |
    +----------------+-----------------------------------------------------------------------------------+


    *******
    Methods
    *******
    +-----------------------------------------------+------------------------------------------------------------+
    | :ref:`fit(self, X, y, t) <eco_fit>`           | Build an econometric model from the training set (X, y, t).|
    +-----------------------------------------------+------------------------------------------------------------+
    | :ref:`predict(self, X, t=None) <eco_predict>` | Predict an uplift for X.                                   |
    +-----------------------------------------------+------------------------------------------------------------+
    """

    def __init__(self, model=LinearRegression()):
        try:
            model.__getattribute__('fit')
            model.__getattribute__('predict')
        except AttributeError:
            raise ValueError('Model should contains two methods: fit and predict.')
        self.model = model

    def fit(self, X, y, t):
        """Build an econometric model from the training set (X, y, t).

        +------------------+---------------------------------------------------------------------------------+
        | **Parameters**   | | **X: numpy ndarray with shape = [n_samples, n_features]**                     |
        |                  | |   Matrix of features.                                                         |
        |                  | | **y: numpy array with shape = [n_samples,]**                                  |
        |                  | |   Array of target of feature.                                                 |
        |                  | | **t: numpy array with shape = [n_samples,]**                                  |
        |                  | |   Array of treatments.                                                        |
        +------------------+---------------------------------------------------------------------------------+
        | **Returns**      | **self : object**                                                               |
        +------------------+---------------------------------------------------------------------------------+
        """

        x_train = self.__get_matrix(X, t)
        self.model.fit(x_train, y)
        return self

    def predict(self, X, t=None):
        """Predict an uplift for X.

        +------------------+---------------------------------------------------------------------------------+
        | **Parameters**   | | **X: numpy ndarray with shape = [n_samples, n_features]**                     |
        |                  | |   Matrix of features.                                                         |
        |                  | | **t: numpy array with shape = [n_samples,] or None**                          |
        |                  | |   Array of treatments.                                                        |
        +------------------+---------------------------------------------------------------------------------+
        | **Returns**      | | **self : object**                                                             |
        |                  | |   The predicted values.                                                       |
        +------------------+---------------------------------------------------------------------------------+
        """

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
