import numpy as np
from sklearn.linear_model import LogisticRegression

from .base import TransformationBaseModel


class Jaskowski(TransformationBaseModel):
    """The class which implements the Jaskowski's approach.

    +----------------+-----------------------------------------------------------------------------------+
    | **Parameters** | | **model : object, optional (default=sklearn.linear_model.LogisticRegression)**  |
    |                | |   The classification model which will be used for predict uplift.               |
    +----------------+-----------------------------------------------------------------------------------+


    *******
    Methods
    *******
    +-----------------------------------------------+----------------------------------------------------+
    | :ref:`fit(self, X, y, t) <jask_fit>`          | Build the model from the training set (X, y, t).   |
    +-----------------------------------------------+----------------------------------------------------+
    | :ref:`predict(self, X, t=None) <jask_predict>`| Predict an uplift for X.                           |
    +-----------------------------------------------+----------------------------------------------------+
    """

    def __init__(self, model=LogisticRegression(n_jobs=-1)):
        try:
            model.__getattribute__('fit')
            model.__getattribute__('predict')
        except AttributeError:
            raise ValueError('Model should contains two methods: fit and predict.')
        self.model = model

    def fit(self, X, y, t):
        """Build the model from the training set (X, y, t).

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

        y_encoded = self.__encode_data(y, t)
        self.model.fit(X, y_encoded)
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

        p = self.model.predict_proba(X)[:, 1]
        return 2 * p - 1

    def __encode_data(self, y, t):
        y_values = []
        for i in range(y.shape[0]):
            if self.is_tr(y[i], t[i]) or self.is_cn(y[i], t[i]):
                y_values.append(1)
            else:
                y_values.append(0)
        return np.array(y_values)
