################
train_test_split
################

Split X, y, t into random train and test subsets.

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

********
Examples
********

.. code-block:: python3

   from pyuplift.model_selection import train_test_split
   ...
   for seed in seeds:
       X_train, X_test, y_train, y_test, t_train, t_test = train_test_split(X, y, t, train_share, seed)
       model.fit(X_train, y_train, t_train)
       score = get_average_effect(y_test, t_test, model.predict(X_test))
       scores.append(score)
