import pytest
from sklearn.ensemble import RandomForestRegressor
from pyuplift.variable_selection import TwoModel
from .base import *


def test_two_model__right_class():
    reg_model = RandomForestRegressor()
    TwoModel(reg_model, reg_model)


def test_two_model__empty_class():
    reg_model = EmptyClass()
    with pytest.raises(ValueError):
        TwoModel(reg_model, reg_model)


def test_two_model__non_fit_class():
    reg_model = NoFitClass()
    with pytest.raises(ValueError):
        TwoModel(reg_model, reg_model)


def test_two_model__non_predict_class():
    reg_model = NoPredictClass()
    with pytest.raises(ValueError):
        TwoModel(reg_model, reg_model)
