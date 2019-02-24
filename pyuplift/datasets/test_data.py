import numpy as np
import pandas as pd


def load_test_data(size: int, seed=777):
    """Data generator.

    The data generates by formula:
    Y = X1 + X2 * T + eps, where
    X1 ~ N(0, 10),
    X2 ~ N(0, 1),
    X3 ~ N(0, 10),
    T ~ R((0, 1), 0.5),
    eps ~ N(0, 10)
    Parameters
    ----------
    size : int.
         The number of splits.
    seed : int, default: 777
         The random seed.
    Returns
    -------
    data : pandas DataFrame
    """

    np.random.seed(seed)
    x1 = np.random.normal(0, 10, size)
    x2 = np.random.normal(0, 1, size)
    x3 = np.random.normal(0, 10, size)
    t = np.random.randint(0, 2, size)
    e = np.random.normal(0, 10, size)
    y = [(x1[i] + x2[i] * t[i] + e[i]) for i in range(size)]

    return pd.DataFrame(data={
        'x1': x1,
        'x2': x2,
        'x3': x3,
        't': t,
        'y': y
    })
