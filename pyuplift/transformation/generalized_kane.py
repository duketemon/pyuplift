from sklearn.ensemble import RandomForestClassifier

from .kane import Kane


class GeneralizedKane(Kane):
    """Generalized Kane approach.
    Method description available in the article
    "A Literature Survey and Experimental Evaluation of the State-of-the-Art in Uplift Modeling:
    A Stepping Stone Toward the Development of Prescriptive Analytics"
    by Floris Devriendt, Darie Moldovan, and Wouter Verbeke
    """

    def __init__(self, model=RandomForestClassifier(n_jobs=-1)):
        super(Kane, self).__init__(model)

    def __get_treatment_count(self, t):
        return sum([el for el in t if el != 0])

    def __get_control_count(self, t):
        return sum([el for el in t if el == 0])

    def fit(self, X, y, t):
        """The method description you can find in the base class"""
        y_encoded = self._encode_data(y, t)
        self.model.fit(X, y_encoded)
        self.control_count = self.__get_control_count(t)
        self.treatment_count = self.__get_treatment_count(t)
        return self

    def predict(self, X, t=None):
        """The method description you can find in the base class"""
        p_tr = self.model.predict_proba(X)[:, 0]
        p_cn = self.model.predict_proba(X)[:, 1]
        p_tn = self.model.predict_proba(X)[:, 2]
        p_cr = self.model.predict_proba(X)[:, 3]
        return (p_tr / self.treatment_count + p_cn / self.control_count) - \
               (p_tn / self.treatment_count + p_cr / self.control_count)
