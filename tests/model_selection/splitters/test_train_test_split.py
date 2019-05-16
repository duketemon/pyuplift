import pytest
import numpy as np
from pyuplift.datasets import make_linear_regression
from pyuplift.model_selection import train_test_split


def test_train_test_split__default():
    size = 1000
    df = make_linear_regression(size)
    X, y, t = df.drop(['y', 't'], axis=1).values, df['y'].values, df['t'].values
    X_train, X_test, y_train, y_test, t_train, t_test = train_test_split(X, y, t, random_state=10)

    assert X_train.shape[0] == 700
    assert X_test.shape[0] == 300
    assert y_train.shape[0] == 700
    assert y_test.shape[0] == 300
    assert t_train.shape[0] == 700
    assert t_test.shape[0] == 300


def test_train_test_split__repeated_random_state():
    random_state, size = 101, 1000

    df = make_linear_regression(size, random_state=random_state)
    X, y, t = df.drop(['y', 't'], axis=1).values, df['y'].values, df['t'].values
    X_train1, X_test1, y_train1, y_test1, t_train1, t_test1 = train_test_split(X, y, t, random_state=random_state)

    df = make_linear_regression(size, random_state=random_state)
    X, y, t = df.drop(['y', 't'], axis=1).values, df['y'].values, df['t'].values
    X_train2, X_test2, y_train2, y_test2, t_train2, t_test2 = train_test_split(X, y, t, random_state=random_state)

    assert np.array_equal(X_train1, X_train2)
    assert np.array_equal(X_test1, X_test2)
    assert np.array_equal(y_train1, y_train2)
    assert np.array_equal(y_test1, y_test2)
    assert np.array_equal(t_train1, t_train2)
    assert np.array_equal(t_test1, t_test2)


def test_train_test_split__none_random_state():
    random_state, size = 101, 1000

    df = make_linear_regression(size, random_state=random_state)
    X, y, t = df.drop(['y', 't'], axis=1).values, df['y'].values, df['t'].values
    X_train1, X_test1, y_train1, y_test1, t_train1, t_test1 = train_test_split(X, y, t, random_state=None)

    df = make_linear_regression(size, random_state=random_state)
    X, y, t = df.drop(['y', 't'], axis=1).values, df['y'].values, df['t'].values
    X_train2, X_test2, y_train2, y_test2, t_train2, t_test2 = train_test_split(X, y, t, random_state=None)

    assert not np.array_equal(X_train1, X_train2)


def test_train_test_split__negative_train_share():
    random_state, size = 101, 1000
    df = make_linear_regression(size, random_state=random_state)
    X, y, t = df.drop(['y', 't'], axis=1).values, df['y'].values, df['t'].values

    with pytest.raises(ValueError):
        train_test_split(X, y, t, train_share=-0.5)


def test_train_test_split__zero_train_share():
    random_state, size = 101, 1000
    df = make_linear_regression(size, random_state=random_state)
    X, y, t = df.drop(['y', 't'], axis=1).values, df['y'].values, df['t'].values

    with pytest.raises(ValueError):
        train_test_split(X, y, t, train_share=0)
