import numpy as np
from sklearn.linear_model import LinearRegression
from pyuplift import BaseModel


class Dummy(BaseModel):
    """The class which implements the dummy approach.

    +----------------+-----------------------------------------------------------------------------------+
    | **Parameters** | | **model : object, optional (default=sklearn.linear_model.LinearRegression)**    |
    |                | |   The regression model which will be used for predict uplift.                   |
    +----------------+-----------------------------------------------------------------------------------+


    *******
    Methods
    *******
    +-------------------------------------------------+-----------------------------------------------------+
    | :ref:`fit(self, X, y, t) <dummy_fit>`           | Build a dummy model from the training set (X, y, t).|
    +-------------------------------------------------+-----------------------------------------------------+
    | :ref:`predict(self, X, t=None) <dummy_predict>` | Predict an uplift for X.                            |
    +-------------------------------------------------+-----------------------------------------------------+
    """

    def __init__(self, model=LinearRegression()):
        try:
            model.__getattribute__('fit')
            model.__getattribute__('predict')
        except AttributeError:
            raise ValueError('Model should contains two methods: fit and predict.')
        self.model = model

    def fit(self, X, y, t):
        """Build a dummy model from the training set (X, y, t).

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

        x_train = np.append(X, t.reshape((-1, 1)), axis=1)
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

        col = np.array(X.shape[0] * [0])
        x_test = np.append(X, col.reshape((-1, 1)), axis=1)
        # All treatment values == 0
        s0 = self.model.predict(x_test)
        x_test[:, -1] = 1
        # All treatment values == 1
        s1 = self.model.predict(x_test)
        return s1 - s0
