import pytest
import numpy as np
from pyuplift.datasets import make_linear_regression


def test_make_linear_regression__repeated_random_state():
    random_state, size = 101, 1000
    df1 = make_linear_regression(size, random_state=random_state)
    df2 = make_linear_regression(size, random_state=random_state)

    assert np.array_equal(df1['x1'].values, df2['x1'].values)
    assert np.array_equal(df1['x2'].values, df2['x2'].values)
    assert np.array_equal(df1['x3'].values, df2['x3'].values)
    assert np.array_equal(df1['t'].values, df2['t'].values)
    assert np.array_equal(df1['y'].values, df2['y'].values)


def test_make_linear_regression__none_random_state():
    size = 1000
    df1 = make_linear_regression(size, random_state=None)
    df2 = make_linear_regression(size, random_state=None)

    assert not np.array_equal(df1['x1'].values, df2['x1'].values)


def test_make_linear_regression__zero_size():
    with pytest.raises(ValueError):
        make_linear_regression(0)


def test_make_linear_regression__negative_size():
    with pytest.raises(ValueError):
        make_linear_regression(-10)
