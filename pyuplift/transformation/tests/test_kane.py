import pytest
from sklearn.ensemble import RandomForestClassifier
from ..kane import Kane
from .test import *


def test_kane__right_class():
    model = RandomForestClassifier()
    Kane(model)


def test_kane__empty_class():
    model = EmptyClass()
    with pytest.raises(ValueError):
        Kane(model)


def test_kane__non_fit_class():
    model = NoFitClass()
    with pytest.raises(ValueError):
        Kane(model)


def test_kane__non_predict_class():
    model = NoPredictClass()
    with pytest.raises(ValueError):
        Kane(model)
