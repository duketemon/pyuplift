import pytest
from sklearn.ensemble import RandomForestRegressor
from pyuplift.variable_selection import Econometric
from .base import *


def test_econometric__right_class():
    reg_model = RandomForestRegressor()
    Econometric(reg_model)


def test_econometric__empty_class():
    reg_model = EmptyClass()
    with pytest.raises(ValueError):
        Econometric(reg_model)


def test_econometric__non_fit_class():
    reg_model = NoFitClass()
    with pytest.raises(ValueError):
        Econometric(reg_model)


def test_econometric__non_predict_class():
    reg_model = NoPredictClass()
    with pytest.raises(ValueError):
        Econometric(reg_model)
