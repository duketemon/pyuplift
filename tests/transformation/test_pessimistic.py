import pytest
from sklearn.ensemble import RandomForestClassifier
from pyuplift.transformation import Pessimistic
from .base import *


def test_pessimistic__right_class():
    model = RandomForestClassifier()
    Pessimistic(model)


def test_pessimistic__empty_class():
    model = EmptyClass()
    with pytest.raises(ValueError):
        Pessimistic(model)


def test_pessimistic__non_fit_class():
    model = NoFitClass()
    with pytest.raises(ValueError):
        Pessimistic(model)


def test_pessimistic__non_predict_class():
    model = NoPredictClass()
    with pytest.raises(ValueError):
        Pessimistic(model)
