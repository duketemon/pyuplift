from sklearn.linear_model import LinearRegression
from pyuplift import BaseModel


class TwoModel(BaseModel):
    """The class which implements the two model approach.

    +----------------+---------------------------------------------------------------------------------------------+
    | **Parameters** | | **no_treatment_model : object, optional (default=sklearn.linear_model.LinearRegression)** |
    |                | |   The regression model which will be used for predict uplift.                             |
    |                | | **has_treatment_model : object, optional (default=sklearn.linear_model.LinearRegression)**|
    |                | |   The regression model which will be used for predict uplift.                             |
    +----------------+---------------------------------------------------------------------------------------------+

    *******
    Methods
    *******
    +-----------------------------------------------+--------------------------------------------------------------+
    | :ref:`fit(self, X, y, t) <two_fit>`           | Build a two model model from the training set (X, y, t).     |
    +-----------------------------------------------+--------------------------------------------------------------+
    | :ref:`predict(self, X, t=None) <two_predict>` | Predict an uplift for X.                                     |
    +-----------------------------------------------+--------------------------------------------------------------+
    """

    def __init__(self, no_treatment_model=LinearRegression(), has_treatment_model=LinearRegression()):
        try:
            no_treatment_model.__getattribute__('fit')
            no_treatment_model.__getattribute__('predict')
        except AttributeError:
            raise ValueError('No treatment model should contains two methods: fit and predict.')

        try:
            has_treatment_model.__getattribute__('fit')
            has_treatment_model.__getattribute__('predict')
        except AttributeError:
            raise ValueError('Has treatment model should contains two methods: fit and predict.')

        self.no_treatment_model = no_treatment_model
        self.has_treatment_model = has_treatment_model

    def fit(self, X, y, t):
        """Build a model model model from the training set (X, y, t).

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

        no_treatment_x, no_treatment_y = [], []
        has_treatment_x, has_treatment_y = [], []
        for idx, el in enumerate(t):
            if el:
                has_treatment_x.append(X[idx])
                has_treatment_y.append(y[idx])
            else:
                no_treatment_x.append(X[idx])
                no_treatment_y.append(y[idx])
        self.no_treatment_model.fit(no_treatment_x, no_treatment_y)
        self.has_treatment_model.fit(has_treatment_x, has_treatment_y)
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

        s1 = self.has_treatment_model.predict(X)
        s0 = self.no_treatment_model.predict(X)
        return s1 - s0
