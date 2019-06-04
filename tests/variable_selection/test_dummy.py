import pytest
from sklearn.ensemble import RandomForestRegressor
from pyuplift.variable_selection import Dummy
from .base import *


def test_dummy__right_class():
    reg_model = RandomForestRegressor()
    Dummy(reg_model)


def test_dummy__empty_class():
    reg_model = EmptyClass()
    with pytest.raises(ValueError):
        Dummy(reg_model)


def test_dummy__non_fit_class():
    reg_model = NoFitClass()
    with pytest.raises(ValueError):
        Dummy(reg_model)


def test_dummy__non_predict_class():
    reg_model = NoPredictClass()
    with pytest.raises(ValueError):
        Dummy(reg_model)
