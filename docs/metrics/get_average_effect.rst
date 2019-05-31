##################
get_average_effect
##################

Estimating an average effect of the test set.

+-----------------+----------------------------------------------------------------------------------+
| **Parameters:** | | **y_test**: numpy array                                                        |
|                 | |   Actual y values.                                                             |
|                 | | **t_test**: numpy array                                                        |
|                 | |   Actual treatment values.                                                     |
|                 | | **y_pred**: numpy array                                                        |
|                 | |   Predicted y values by uplift model.                                          |
|                 | | **test_share**: float                                                          |
|                 | |   Share of the test data which will be taken for estimating an average effect. |
+-----------------+----------------------------------------------------------------------------------+
| **Returns:**    | | **average effect**: float                                                      |
|                 | |   Average effect on the test set.                                              |
+-----------------+----------------------------------------------------------------------------------+

********
Examples
********

.. code-block:: python3

   from pyuplift.metrics import get_average_effect
   ...
   train_indexes, test_indexes = train_test_split_indexes(y, train_share, seed)
   model.fit(X[train_indexes, :], y[train_indexes], t[train_indexes])
   effect = get_average_effect(
          y[test_indexes],
          t[test_indexes],
          model.predict(X[test_indexes, :])
   )
   print(effect)
