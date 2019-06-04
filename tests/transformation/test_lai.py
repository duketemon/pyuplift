import pytest
from sklearn.ensemble import RandomForestClassifier
from pyuplift.transformation import Lai
from .base import *


def test_lai__right_class():
    model = RandomForestClassifier()
    Lai(model)


def test_lai__empty_class():
    model = EmptyClass()
    with pytest.raises(ValueError):
        Lai(model)


def test_lai__non_fit_class():
    model = NoFitClass()
    with pytest.raises(ValueError):
        Lai(model)


def test_lai__non_predict_class():
    model = NoPredictClass()
    with pytest.raises(ValueError):
        Lai(model)
