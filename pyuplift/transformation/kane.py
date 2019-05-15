import numpy as np
from sklearn.linear_model import LogisticRegression

from .base import TransformationBaseModel


class Kane(TransformationBaseModel):
    """The class which implements the Kane's approach.

    +----------------+-----------------------------------------------------------------------------------+
    | **Parameters** | | **model : object, optional (default=sklearn.linear_model.LogisticRegression)**  |
    |                | |   The classification model which will be used for predict uplift.               |
    |                | | **use_weights : boolean, optional (default=False)**                             |
    |                | |   Use or not weights?                                                           |
    +----------------+-----------------------------------------------------------------------------------+


    *******
    Methods
    *******
    +-----------------------------------------------+----------------------------------------------------+
    | :ref:`fit(self, X, y, t) <lai_fit>`           | Build the model from the training set (X, y, t).   |
    +-----------------------------------------------+----------------------------------------------------+
    | :ref:`predict(self, X, t=None) <lai_predict>` | Predict an uplift for X.                           |
    +-----------------------------------------------+----------------------------------------------------+
    """

    def __init__(self, model=LogisticRegression(n_jobs=-1), use_weights=False):
        try:
            model.__getattribute__('fit')
            model.__getattribute__('predict')
        except AttributeError:
            raise ValueError('Model should contains two methods: fit and predict.')
        self.model = model
        self.use_weights = use_weights

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
        if self.use_weights:
            self.__init_weights(t)
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

        p_tr = self.model.predict_proba(X)[:, 0]
        p_cn = self.model.predict_proba(X)[:, 1]
        p_tn = self.model.predict_proba(X)[:, 2]
        p_cr = self.model.predict_proba(X)[:, 3]
        if self.use_weights:
            return (p_tr / self.treatment_count + p_cn / self.control_count) - \
                   (p_tn / self.treatment_count + p_cr / self.control_count)
        else:
            return (p_tr + p_cn) - (p_tn + p_cr)

    def __encode_data(self, y, t):
        y_values = []
        for i in range(y.shape[0]):
            if self.is_tr(y[i], t[i]):
                y_values.append(0)
            elif self.is_cn(y[i], t[i]):
                y_values.append(1)
            elif self.is_tn(y[i], t[i]):
                y_values.append(2)
            elif self.is_cr(y[i], t[i]):
                y_values.append(3)
        return np.array(y_values)

    def __init_weights(self, t):
        control_count, treatment_count = 0, 0
        for el in t:
            if el == 0.0:
                control_count += 1
            else:
                treatment_count += 1
        self.control_count = control_count
        self.treatment_count = treatment_count
