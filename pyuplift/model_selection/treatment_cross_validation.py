from pyuplift.metrics import get_average_effect
from .train_test_split_indexes import train_test_split_indexes


def treatment_cross_val_score(X, y, t, model, cv=5, train_share=0.7, seeds=None):
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
    cv : int, default: 5
         The number of splits.
    train_share : callable, default: 0.7
        The `test_share` should be between 0.0 and 1.0 and represent the
        proportion of the dataset to predict effect.
    seeds : array, default: None
        The array of seeds for random generator
    Returns
    -------
    scores : numpy array of floats
    """

    if seeds is None:
        seeds = [None for _ in range(cv)]

    if cv != len(seeds):
        raise Exception("The length of seed's array  should be equals to cv.")

    scores = []
    for i in range(cv):
        train_indexes, test_indexes = train_test_split_indexes(y, train_share, seeds[i])
        model.fit(X[train_indexes, :], y[train_indexes], t[train_indexes])
        score = get_average_effect(
            y[test_indexes],
            t[test_indexes],
            model.predict(X[test_indexes, :])
        )
        scores.append(score)
    return scores
