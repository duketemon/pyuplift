import numpy as np

from pyuplift.metrics import get_average_effect
from pyuplift.model_selection import train_test_split


def treatment_cross_val_score(X, y, t, model, cv=5, train_share=0.7, seeds=None):
    """Evaluate a scores by cross-validation.

    +------------------+-----------------------------------------------------------------------------------------+
    | **Parameters**   | | **X: numpy ndarray with shape = [n_samples, n_features]**                             |
    |                  | |   Matrix of features.                                                                 |
    |                  | | **y: numpy array with shape = [n_samples,]**                                          |
    |                  | |   Array of target of feature.                                                         |
    |                  | | **t: numpy array with shape = [n_samples,]**                                          |
    |                  | |   Array of treatments.                                                                |
    |                  | | **train_share: float, optional (default=0.7)**                                        |
    |                  | |   train_share represents the proportion of the dataset to include in the train split. |
    |                  | | **random_state: int, optional (default=777)**                                         |
    |                  | |   random_state is the seed used by the random number generator.                       |
    +------------------+-----------------------------------------------------------------------------------------+
    | **Return**       | | **scores: numpy array of floats**                                                     |
    |                  | |   Array of scores of the estimator for each run of the cross validation.              |
    +------------------+-----------------------------------------------------------------------------------------+
    """

    if seeds is None:
        seeds = [None for _ in range(cv)]

    if cv < 1:
        raise ValueError('Count of validations should be positive integer number.')
    elif cv != len(seeds):
        raise ValueError("The length of seed's array should be equals to cv.")
    elif not (0 < train_share <= 1):
        raise ValueError('Train share should be float number between 0 and 1.')

    scores = []
    for seed in seeds:
        X_train, X_test, y_train, y_test, t_train, t_test = train_test_split(X, y, t, train_share, seed)
        model.fit(X_train, y_train, t_train)
        score = get_average_effect(y_test, t_test, model.predict(X_test))
        scores.append(score)
    return np.array(scores)
