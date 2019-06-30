import numpy as np
from sklearn.linear_model import LinearRegression
from pyuplift import BaseModel


class Cadit(BaseModel):
    """The class which implements the cadit approach [1].

    +----------------+-----------------------------------------------------------------------------------+
    | **Parameters** | | **model : object, optional (default=sklearn.linear_model.LinearRegression)**    |
    |                | |   The regression model which will be used for predict uplift.                   |
    +----------------+-----------------------------------------------------------------------------------+


    *******
    Methods
    *******
    +-------------------------------------------------+--------------------------------------------------+
    | :ref:`fit(self, X, y, t) <cadit_fit>`           | Build a model from the training set (X, y, t).   |
    +-------------------------------------------------+--------------------------------------------------+
    | :ref:`predict(self, X, t=None) <cadit_predict>` | Predict an uplift for X.                         |
    +-------------------------------------------------+--------------------------------------------------+
    """

    def __init__(self, model=LinearRegression()):
        try:
            model.__getattribute__('fit')
            model.__getattribute__('predict')
        except AttributeError:
            raise ValueError('Model should contains two methods: fit and predict.')
        self.model = model

    def fit(self, X, y, t):
        """Build a model from the training set (X, y, t).

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

        z = self.__get_z_values(y, t)
        self.model.fit(X, z)
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

        return self.model.predict(X)

    def __get_z_values(self, y, t):
        p_t0 = t[t == 0].shape[0] / t.shape[0]
        p_t1 = 1 - p_t0
        y_mean = y.mean()
        z = []
        for i in range(y.shape[0]):
            if t[i] == 0:
                val = (1/p_t1) * (y[i] - y_mean)
            else:
                val = - (1/p_t0) * (y[i] - y_mean)
            z.append(val)
        return np.array(z)
