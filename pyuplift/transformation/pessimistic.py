from sklearn.ensemble import RandomForestClassifier

from .base import TransformationBaseModel
from .weighted_lai import WeightedLai
from .reflective import Reflective


class Pessimistic(TransformationBaseModel):
    """Pessimistic approach.
    Method description available in the article
    "A Literature Survey and Experimental Evaluation of the State-of-the-Art in Uplift Modeling:
    A Stepping Stone Toward the Development of Prescriptive Analytics"
    by Floris Devriendt, Darie Moldovan, and Wouter Verbeke
    """

    def __init__(self, model=RandomForestClassifier(n_jobs=-1)):
        self.w_lai_model = WeightedLai(model)
        self.reflective_model = Reflective(model)

    def fit(self, X, y, t):
        """The method description you can find in the base class"""
        self.w_lai_model.fit(X, y, t)
        self.reflective_model.fit(X, y, t)
        return self

    def predict(self, X, t=None):
        """The method description you can find in the base class"""
        w_lai_uplift = self.w_lai_model.predict(X)
        reflective_uplift = self.reflective_model.predict(X)
        return (w_lai_uplift + reflective_uplift) / 2
