import pytest
from sklearn.ensemble import RandomForestClassifier
from pyuplift.transformation import Jaskowski
from .base import *


def test_jaskowski__right_class():
    model = RandomForestClassifier()
    Jaskowski(model)


def test_jaskowski__empty_class():
    model = EmptyClass()
    with pytest.raises(ValueError):
        Jaskowski(model)


def test_jaskowski__non_fit_class():
    model = NoFitClass()
    with pytest.raises(ValueError):
        Jaskowski(model)


def test_jaskowski__non_predict_class():
    model = NoPredictClass()
    with pytest.raises(ValueError):
        Jaskowski(model)
