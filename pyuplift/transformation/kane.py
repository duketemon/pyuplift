import numpy as np
from sklearn.ensemble import RandomForestClassifier

from .base import TransformationBaseModel


class Kane(TransformationBaseModel):
    """Kane approach.
    Method description available in the article
    "A Literature Survey and Experimental Evaluation of the State-of-the-Art in Uplift Modeling:
    A Stepping Stone Toward the Development of Prescriptive Analytics"
    by Floris Devriendt, Darie Moldovan, and Wouter Verbeke
    """

    def __init__(self, model=RandomForestClassifier(n_jobs=-1)):
        self.model = model

    def _encode_data(self, y, t):
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

    def fit(self, X, y, t):
        """The method description you can find in the base class"""
        y_encoded = self._encode_data(y, t)
        self.model.fit(X, y_encoded)
        return self

    def predict(self, X, t=None):
        """The method description you can find in the base class"""
        p_tr = self.model.predict_proba(X)[:, 0]
        p_cn = self.model.predict_proba(X)[:, 1]
        p_tn = self.model.predict_proba(X)[:, 2]
        p_cr = self.model.predict_proba(X)[:, 3]
        return (p_tr + p_cn) - (p_tn + p_cr)
