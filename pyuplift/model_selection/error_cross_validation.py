import numpy as np
from math import sqrt
from sklearn.metrics import mean_squared_error


def rmse_cross_val_score(x, y, t, model, cv=5):
    """Evaluate a score by cross-validation with  ``Root Mean Squared Error`` score function."""
    rmse = lambda true, pred: sqrt(mean_squared_error(true, pred))
    return cross_val_score(x, y, t, model, rmse, cv)


def cross_val_score(x, y, t, model, func, cv=5):
    """Evaluate a scores by cross-validation

    Parameters
    ----------
    x : numpy array of shape = [n_samples, n_features]
        The training input samples.
    y : numpy array of shape = [n_samples] or [n_samples, n_outputs]
        The target values (class labels in classification, real numbers in regression).
    t : numpy array of shape = [n_samples] or [n_samples, n_outputs]
        The treatments.
    model : Derived class of the BaseModel
        The model of predicting treatment effect.
    func : callable
        The scorer callable object.
    cv : int, default: 5
         The number of splits.
    Returns
    -------
    scores : numpy array of floats
    """
    steps = [0] * cv
    for i in range(len(y)):
        steps[i % cv] += 1
    ind = 0
    scores = []
    for i in range(cv):
        x_train = np.concatenate((x[:ind, :], x[ind + steps[i]:, :]), axis=0)
        y_train = np.append(y[:ind], y[ind + steps[i]:])
        t_train = np.append(t[:ind], t[ind + steps[i]:])
        model.fit(x_train, y_train, t_train)

        x_test = x[ind:ind + steps[i], :]
        y_test = x[ind:ind + steps[i], 1]
        y_pred = model.predict(x_test)

        scores.append(func(y_test, y_pred))
        ind += steps[i]
    return np.array(scores)
