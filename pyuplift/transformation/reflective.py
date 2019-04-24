import numpy as np
from sklearn.ensemble import RandomForestClassifier

from .base import TransformationBaseModel


class Reflective(TransformationBaseModel):
    """Reflective approach.
    Method description available in the article
    "A Literature Survey and Experimental Evaluation of the State-of-the-Art in Uplift Modeling:
    A Stepping Stone Toward the Development of Prescriptive Analytics"
    by Floris Devriendt, Darie Moldovan, and Wouter Verbeke
    """

    def __init__(self, model=RandomForestClassifier(n_jobs=-1)):
        self.model = model

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

    def __set_probabilities(self, y, t):
        t_r, c_r, t_n, c_n = 0, 0, 0, 0
        r_count, n_count = 0, 0
        size = y.shape[0]
        for i in range(size):
            if y[i] != 0:
                r_count += 1
                if t[i] != 0:
                    # T|R
                    t_r += 1
                else:
                    # C|R
                    c_r += 1
            else:
                n_count += 1
                if t[i] != 0:
                    # T|N
                    t_n += 1
                else:
                    # C|N
                    c_n += 1

        self.p_tlr = t_r / r_count
        self.p_clr = c_r / r_count
        self.p_cln = c_n / n_count
        self.p_tln = t_n / n_count

    def fit(self, X, y, t):
        """The method description you can find in the base class"""
        y_encoded = self.__encode_data(y, t)
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
