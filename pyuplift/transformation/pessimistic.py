from sklearn.linear_model import LogisticRegression

from .base import TransformationBaseModel
from .lai import Lai
from .reflective import Reflective


class Pessimistic(TransformationBaseModel):
    """The class which implements the pessimistic approach.

    +----------------+-----------------------------------------------------------------------------------+
    | **Parameters** | | **model : object, optional (default=sklearn.linear_model.LogisticRegression)**  |
    |                | |   The classification model which will be used for predict uplift.               |
    +----------------+-----------------------------------------------------------------------------------+


    *******
    Methods
    *******
    +-----------------------------------------------+----------------------------------------------------+
    | :ref:`fit(self, X, y, t) <pes_fit>`           | Build the model from the training set (X, y, t).   |
    +-----------------------------------------------+----------------------------------------------------+
    | :ref:`predict(self, X, t=None) <pes_predict>` | Predict an uplift for X.                           |
    +-----------------------------------------------+----------------------------------------------------+
    """

    def __init__(self, model=LogisticRegression(n_jobs=-1)):
        try:
            model.__getattribute__('fit')
            model.__getattribute__('predict')
        except AttributeError:
            raise ValueError('Model should contains two methods: fit and predict.')
        self.w_lai_model = Lai(model, use_weights=True)
        self.reflective_model = Reflective(model)

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

        self.w_lai_model.fit(X, y, t)
        self.reflective_model.fit(X, y, t)
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

        w_lai_uplift = self.w_lai_model.predict(X)
        reflective_uplift = self.reflective_model.predict(X)
        return (w_lai_uplift + reflective_uplift) / 2
