import numpy as np
import pandas as pd


def load_linear(
        size: int,
        x1_params=(0, 10),
        x2_params=(0, 1),
        x3_params=(0, 10),
        t_params=(0, 2),
        e_params=(0, 10),
        seed=777
):
    """The data generates by formula:
    Y = X1+X2*T+E

    Parameters
    ----------
    size : int
         The number of observations.
    x1_params : tuple(mu, sigma), default: (0, 10)
         The feature with gaussian distribution and mean=mu, sd=sigma.
         X1 ~ N(mu, sigma)
    x2_params : tuple(mu, sigma), default: (0, 1)
         The feature with gaussian distribution and mean=mu, sd=sigma.
         X2 ~ N(mu, sigma)
    x3_params : tuple(mu, sigma), default: (0, 10)
         The feature with gaussian distribution and mean=mu, sd=sigma.
         X3 ~ N(mu, sigma)
    t_params : tuple(min, max), default: (0, 2)
         The treatment with uniform distribution. Min value=min, Max value=max-1
         T ~ R(min, max)
    e_params : tuple(mu, sigma), default: (0, 10)
         The error with gaussian distribution and mean=mu, sd=sigma.
         E ~ N(mu, sigma)
    seed : int, default: 777
         The random seed.
    Returns
    -------
    data : pandas DataFrame
    """

    np.random.seed(seed)
    x1 = np.random.normal(*x1_params, size)
    x2 = np.random.normal(*x2_params, size)
    x3 = np.random.normal(*x3_params, size)
    t = np.random.randint(*t_params, size)
    e = np.random.normal(*e_params, size)
    y = np.array([(x1[i] + x2[i] * t[i] + e[i]) for i in range(size)])

    return pd.DataFrame(data={
        'x1': x1,
        'x2': x2,
        'x3': x3,
        't': t,
        'y': y
    })


def load_exponential(
        size: int,
        x1_params=(0, 10),
        x2_params=(0, 1),
        x3_params=(0, 10),
        t_params=(0, 2),
        e_params=(0, 10),
        seed=777
):
    """The data generates by formula:
    Y = exp(X1+X2*T)+E

    Parameters
    ----------
    size : int
         The number of observations.
    x1_params : tuple(mu, sigma), default: (0, 10)
         The feature with gaussian distribution and mean=mu, sd=sigma.
         X1 ~ N(mu, sigma)
    x2_params : tuple(mu, sigma), default: (0, 1)
         The feature with gaussian distribution and mean=mu, sd=sigma.
         X2 ~ N(mu, sigma)
    x3_params : tuple(mu, sigma), default: (0, 10)
         The feature with gaussian distribution and mean=mu, sd=sigma.
         X3 ~ N(mu, sigma)
    t_params : tuple(min, max), default: (0, 2)
         The treatment with uniform distribution. Min value=min, Max value=max-1
         T ~ R(min, max)
    e_params : tuple(mu, sigma), default: (0, 10)
         The error with gaussian distribution and mean=mu, sd=sigma.
         E ~ N(mu, sigma)
    seed : int, default: 777
         The random seed.
    Returns
    -------
    data : pandas DataFrame
    """

    np.random.seed(seed)
    x1 = np.random.normal(*x1_params, size)
    x2 = np.random.normal(*x2_params, size)
    x3 = np.random.normal(*x3_params, size)
    t = np.random.randint(*t_params, size)
    e = np.random.normal(*e_params, size)
    y = np.array([(np.exp(x1[i] + x2[i] * t[i]) + e[i]) for i in range(size)])

    return pd.DataFrame(data={
        'x1': x1,
        'x2': x2,
        'x3': x3,
        't': t,
        'y': y
    })


def load_complex(
        size: int,
        x1_params=(0, 10),
        x2_params=(0, 1),
        x3_params=(0, 10),
        t_params=(0, 2),
        e_params=(0, 10),
        seed=777
):
    """The data generates by formula:
    Y = X1^2+exp(X2*T)+E

    Parameters
    ----------
    size : int
         The number of observations.
    x1_params : tuple(mu, sigma), default: (0, 10)
         The feature with gaussian distribution and mean=mu, sd=sigma.
         X1 ~ N(mu, sigma)
    x2_params : tuple(mu, sigma), default: (0, 1)
         The feature with gaussian distribution and mean=mu, sd=sigma.
         X2 ~ N(mu, sigma)
    x3_params : tuple(mu, sigma), default: (0, 10)
         The feature with gaussian distribution and mean=mu, sd=sigma.
         X3 ~ N(mu, sigma)
    t_params : tuple(min, max), default: (0, 2)
         The treatment with uniform distribution. Min value=min, Max value=max-1
         T ~ R(min, max)
    e_params : tuple(mu, sigma), default: (0, 10)
         The error with gaussian distribution and mean=mu, sd=sigma.
         E ~ N(mu, sigma)
    seed : int, default: 777
         The random seed.
    Returns
    -------
    data : pandas DataFrame
    """

    np.random.seed(seed)
    x1 = np.random.normal(*x1_params, size)
    x2 = np.random.normal(*x2_params, size)
    x3 = np.random.normal(*x3_params, size)
    t = np.random.randint(*t_params, size)
    e = np.random.normal(*e_params, size)
    y = np.array([(x1[i] ** 2 + np.exp(x2[i] * t[i]) + e[i]) for i in range(size)])

    return pd.DataFrame(data={
        'x1': x1,
        'x2': x2,
        'x3': x3,
        't': t,
        'y': y
    })

