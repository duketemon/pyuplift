import numpy as np
from sklearn.ensemble import RandomForestClassifier

from .base_model import TransformationBaseModel


class WeightedLai(TransformationBaseModel):
    """Weighted Lai approach.
    Method description available in the article
    "A Literature Survey and Experimental Evaluation of the State-of-the-Art in Uplift Modeling:
    A Stepping Stone Toward the Development of Prescriptive Analytics"
    by Floris Devriendt, Darie Moldovan, and Wouter Verbeke
    """

    def __init__(self, model=RandomForestClassifier(n_jobs=-1)):
        self.model = model

    def __encode_data(self, y, t):
        y_values = []
        self.pos_count = 0
        self.neg_count = 0
        for i in range(y.shape[0]):
            if self.is_tr(y[i], t[i]) or self.is_cn(y[i], t[i]):
                y_values.append(1)
                self.pos_count += 1
            elif self.is_tn(y[i], t[i]) or self.is_cr(y[i], t[i]):
                y_values.append(0)
                self.neg_count += 1
        return np.array(y_values)

    def fit(self, X, y, t):
        """The method description you can find in the base class"""
        y_encoded = self.__encode_data(y, t)
        self.model.fit(X, y_encoded)
        return self

    def predict(self, X, t=None):
        """The method description you can find in the base class"""
        p_tr_cn = self.model.predict_proba(X)[:, 1]
        p_tn_cr = self.model.predict_proba(X)[:, 0]
        return p_tr_cn * (self.pos_count / (self.pos_count + self.neg_count)) - \
               p_tn_cr * (self.neg_count / (self.pos_count + self.neg_count))
