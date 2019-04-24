from sklearn.ensemble import RandomForestClassifier

from .lai import Lai


class WeightedLai(Lai):
    """Weighted Lai approach.
    Method description available in the article
    "A Literature Survey and Experimental Evaluation of the State-of-the-Art in Uplift Modeling:
    A Stepping Stone Toward the Development of Prescriptive Analytics"
    by Floris Devriendt, Darie Moldovan, and Wouter Verbeke
    """

    def __init__(self, model=RandomForestClassifier(n_jobs=-1)):
        super().__init__(model)

    def __set_probabilities(self, y, t):
        pos_count, neg_count = 0, 0
        for i in range(y.shape[0]):
            if self.is_tr(y[i], t[i]) or self.is_cn(y[i], t[i]):
                pos_count += 1
            elif self.is_tn(y[i], t[i]) or self.is_cr(y[i], t[i]):
                neg_count += 1

        self.p_tr_or_cn = pos_count / (pos_count + neg_count)
        self.p_tn_or_cr = neg_count / (pos_count + neg_count)

    def fit(self, X, y, t):
        """The method description you can find in the base class"""
        y_encoded = self._encode_data(y, t)
        self.__set_probabilities(y, t)
        self.model.fit(X, y_encoded)
        return self

    def predict(self, X, t=None):
        """The method description you can find in the base class"""
        p_tr_cn = self.model.predict_proba(X)[:, 1]
        p_tn_cr = self.model.predict_proba(X)[:, 0]
        return p_tr_cn * self.p_tr_or_cn - p_tn_cr * self.p_tn_or_cr
