import numpy as np
from sklearn.linear_model import LogisticRegression

from .base import TransformationBaseModel


class Lai(TransformationBaseModel):
    """The class which implements the Lai's approach.

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
    | :ref:`fit(self, X, y, t) <lai_fit>`           | Build a Lai model from the training set (X, y, t). |
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
        """Build a Lai model from the training set (X, y, t).

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
        if self.use_weights:
            self.__init_weights(y, t)
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

        p_tr_cn = self.model.predict_proba(X)[:, 1]
        if self.use_weights:
            p_tn_cr = self.model.predict_proba(X)[:, 0]
            return p_tr_cn * self.p_tr_or_cn - p_tn_cr * self.p_tn_or_cr
        else:
            return 2 * p_tr_cn - 1

    def __encode_data(self, y, t):
        y_values = []
        for i in range(y.shape[0]):
            if self.is_tr(y[i], t[i]) or self.is_cn(y[i], t[i]):
                y_values.append(1)
            elif self.is_tn(y[i], t[i]) or self.is_cr(y[i], t[i]):
                y_values.append(0)
        return np.array(y_values)

    def __init_weights(self, y, t):
        pos_count, neg_count = 0, 0
        for i in range(y.shape[0]):
            if self.is_tr(y[i], t[i]) or self.is_cn(y[i], t[i]):
                pos_count += 1
            elif self.is_tn(y[i], t[i]) or self.is_cr(y[i], t[i]):
                neg_count += 1

        self.p_tr_or_cn = pos_count / (pos_count + neg_count)
        self.p_tn_or_cr = neg_count / (pos_count + neg_count)
