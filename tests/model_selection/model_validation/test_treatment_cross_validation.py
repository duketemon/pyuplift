import pytest
from pyuplift.variable_selection import Dummy
from pyuplift.datasets import make_linear_regression
from pyuplift.model_selection import treatment_cross_val_score


model = Dummy()
random_state = 101
size = 1000
train_share = 0.7
df = make_linear_regression(size, random_state=random_state)
X, y, t = df.drop(['y', 't'], axis=1).values, df['y'].values, df['t'].values


def test_treatment_cross_val_score__seeds_are_none():
    cv, seeds = 5, None
    scores = treatment_cross_val_score(X, y, t, model, cv, train_share, seeds)
    assert len(scores) == cv


def test_treatment_cross_val_score__cv_not_equals_len_of_seeds():
    cv, seeds = 5, list(range(3))
    with pytest.raises(ValueError):
        treatment_cross_val_score(X, y, t, model, cv, train_share, seeds)


def test_treatment_cross_val_score__negative_cv():
    cv, seeds = -5, list(range(3))
    with pytest.raises(ValueError):
        treatment_cross_val_score(X, y, t, model, cv, train_share, seeds)


def test_treatment_cross_val_score__zero_cv():
    cv, seeds = 0, list(range(3))
    with pytest.raises(ValueError):
        treatment_cross_val_score(X, y, t, model, cv, train_share, seeds)


def test_treatment_cross_val_score__negative_train_share():
    train_share = -0.7
    cv, seeds = 3, list(range(3))
    with pytest.raises(ValueError):
        treatment_cross_val_score(X, y, t, model, cv, train_share, seeds)


def test_treatment_cross_val_score__zero_train_share():
    train_share = 0
    cv, seeds = 3, list(range(3))
    with pytest.raises(ValueError):
        treatment_cross_val_score(X, y, t, model, cv, train_share, seeds)
