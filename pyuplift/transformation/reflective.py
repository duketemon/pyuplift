import numpy as np
from sklearn.ensemble import RandomForestClassifier

from .base_model import TransformationBaseModel


class Reflective(TransformationBaseModel):
    """Reflective approach.
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

    def __set_probabilities(self, y, t):
        r_count, t_count = 0, 0
        for i in range(y.shape[0]):
            if y[i] != 0:
                r_count += 1
                if t[i] == 1:
                    t_count += 1
        self.p_tlr = t_count / r_count
        self.p_clr = (r_count - t_count) / r_count

        n_count, t_count = 0, 0
        for i in range(y.shape[0]):
            if y[i] == 0:
                n_count += 1
                if t[i] == 1:
                    t_count += 1
        self.p_cln = (n_count - t_count) / n_count
        self.p_tln = t_count / n_count

    def fit(self, X, y, t):
        """The method description you can find in the base class"""
        y_encoded = self._encode_data(y, t)
        self.model.fit(X, y_encoded)
        self.__set_probabilities(y, t)
        return self

    def predict(self, X, t=None):
        """The method description you can find in the base class"""
        p_tr = self.model.predict_proba(X)[:, 0]
        p_cn = self.model.predict_proba(X)[:, 1]
        p_tn = self.model.predict_proba(X)[:, 2]
        p_cr = self.model.predict_proba(X)[:, 3]

        p_pos = self.p_tlr * p_tr + self.p_cln * p_cn
        p_neg = self.p_tln * p_tn + self.p_clr * p_cr
        return p_pos - p_neg
