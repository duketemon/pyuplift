def train_test_split(x, y, t, train_share=0.7):
    """Split data (x, y, t) on two parts: train and test

    Parameters
    ----------
    x : numpy array of shape = [n_samples, n_features]
        The training input samples.
    y : numpy array of shape = [n_samples] or [n_samples, n_outputs]
        The target values (class labels in classification, real numbers in regression).
    t : numpy array of shape = [n_samples] or [n_samples, n_outputs]
        The treatments.
    train_share : float, (default=0.7)
        The ``train_share`` should be between 0.0 and 1.0 and represent the
        proportion of the dataset to include in the train split.
    Returns
    -------
    splitting : Tuple
        Tuple containing train-test split of inputs.
    """
    train_part_len = int(train_share * len(y))
    x_train = x[:train_part_len, :]
    x_test = x[train_part_len:, :]

    y_train = y[:train_part_len]
    y_test = y[train_part_len:]

    t_train = t[:train_part_len]
    t_test = t[train_part_len:]
    return (x_train, y_train, t_train), (x_test, y_test, t_test)
