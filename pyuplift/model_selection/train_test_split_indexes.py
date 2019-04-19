import random


def train_test_split_indexes(y, train_share=0.7, seed=None):
    """Splitting data on train and test with proportions

    Parameters
    ----------
    y : numpy array of shape = [n_samples] or [n_samples, n_outputs]
        The target values (class labels in classification, real numbers in regression).
    train_share : float, default=0.7
        The ``train_share`` should be between 0.0 and 1.0 and represent the
        proportion of the dataset to include in the train split.
    seed : int, default=None
        The seed for random generator
    Returns
    -------
    splitting : Tuple
        Tuple containing train-test split of inputs.
    """

    random.seed(seed)
    zeros, non_zeros = [], []
    size = len(y)
    for i in range(size):
        if y[i] == 0:
            zeros.append(i)
        else:
            non_zeros.append(i)
    zero_train_size = int(len(zeros) * train_share)
    non_zero_train_size = int(len(non_zeros) * train_share)
    train_indexes = random.sample(zeros, zero_train_size) + random.sample(non_zeros, non_zero_train_size)
    test_indexes = [i for i in range(size) if i not in train_indexes]
    train_indexes.sort()
    test_indexes.sort()
    return train_indexes, test_indexes
