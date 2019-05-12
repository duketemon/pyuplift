import random


def train_test_split(X, y, t, train_share=0.7, random_state=None):
    """Split X, y, t into random train and test subsets.

    +------------------+-----------------------------------------------------------------------------------------+
    | **Parameters**   | | **X: numpy ndarray with shape = [n_samples, n_features]**                             |
    |                  | |   Matrix of features.                                                                 |
    |                  | | **y: numpy array with shape = [n_samples,]**                                          |
    |                  | |   Array of target of feature.                                                         |
    |                  | | **t: numpy array with shape = [n_samples,]**                                          |
    |                  | |   Array of treatments.                                                                |
    |                  | | **train_share: float, optional (default=0.7)**                                        |
    |                  | |   train_share represents the proportion of the dataset to include in the train split. |
    |                  | | **random_state: int, optional (default=None)**                                        |
    |                  | |   random_state is the seed used by the random number generator.                       |
    +------------------+-----------------------------------------------------------------------------------------+
    | **Return**       | | **X_train: numpy ndarray**                                                            |
    |                  | |   Train matrix of features.                                                           |
    |                  | | **X_test: numpy ndarray**                                                             |
    |                  | |   Test matrix of features.                                                            |
    |                  | | **y_train: numpy array**                                                              |
    |                  | |   Train array of target of feature.                                                   |
    |                  | | **y_test: numpy array**                                                               |
    |                  | |   Test array of target of feature.                                                    |
    |                  | | **t_train: numpy array**                                                              |
    |                  | |   Train array of treatments.                                                          |
    |                  | | **t_test: numpy array**                                                               |
    |                  | |   Test array of treatments.                                                           |
    +------------------+-----------------------------------------------------------------------------------------+
    """

    random.seed(random_state)
    size = len(y)
    train_part_size = int(train_share * size)
    train_index = random.sample([i for i in range(size)], train_part_size)
    test_index = [i for i in range(size) if i not in train_index]

    X_train = X[train_index, :]
    X_test = X[test_index, :]

    y_train = y[train_index]
    y_test = y[test_index]

    t_train = t[train_index]
    t_test = t[test_index]
    return X_train, X_test, y_train, y_test, t_train, t_test
