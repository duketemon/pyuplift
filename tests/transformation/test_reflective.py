import pytest
from sklearn.ensemble import RandomForestClassifier
from pyuplift.transformation import Reflective
from .base import *


def test_reflective__right_class():
    model = RandomForestClassifier()
    Reflective(model)


def test_reflective__empty_class():
    model = EmptyClass()
    with pytest.raises(ValueError):
        Reflective(model)


def test_reflective__non_fit_class():
    model = NoFitClass()
    with pytest.raises(ValueError):
        Reflective(model)


def test_reflective__non_predict_class():
    model = NoPredictClass()
    with pytest.raises(ValueError):
        Reflective(model)
