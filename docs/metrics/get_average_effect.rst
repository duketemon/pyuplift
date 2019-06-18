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
   model.fit(X_train, y_train, t_train)
   y_pred = model.predict(X_test)
   effect = get_average_effect(y_test, t_test, y_pred, test_share)
   print(effect)
