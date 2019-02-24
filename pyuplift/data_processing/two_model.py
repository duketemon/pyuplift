from sklearn.linear_model import LinearRegression
from pyuplift import BaseModel


class TwoModel(BaseModel):
    """TwoModel approach.
    Building two independent models and predicting effect as difference.
    Method description available in the article
    "A Literature Survey and Experimental Evaluation of the State-of-the-Art in Uplift Modeling:
    A Stepping Stone Toward the Development of Prescriptive Analytics"
    by Floris Devriendt, Darie Moldovan, and Wouter Verbeke
    """
    def __init__(self, no_treatment_model=LinearRegression(), has_treatment_model=LinearRegression()):
        self.no_treatment_model = no_treatment_model
        self.has_treatment_model = has_treatment_model

    def fit(self, x, y, t):
        """The method description you can find in the base class"""
        no_treatment_x, no_treatment_y = [], []
        has_treatment_x, has_treatment_y = [], []
        for idx, el in enumerate(t):
            if el:
                has_treatment_x.append(x[idx])
                has_treatment_y.append(y[idx])
            else:
                no_treatment_x.append(x[idx])
                no_treatment_y.append(y[idx])

        return self.fit2(no_treatment_x, no_treatment_y, has_treatment_x, has_treatment_y)

    def predict(self, x, t=None):
        """The method description you can find in the base class"""
        return self.has_treatment_model.predict(x) - self.no_treatment_model.predict(x)

    def fit2(self, no_treatment_x, no_treatment_y, has_treatment_x, has_treatment_y):
        """The alternative fitting method"""
        self.no_treatment_model.fit(no_treatment_x, no_treatment_y)
        self.has_treatment_model.fit(has_treatment_x, has_treatment_y)
        return self
