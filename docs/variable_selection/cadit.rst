#####
Cadit
#####

The class which implements the cadit approach [1].

+----------------+-----------------------------------------------------------------------------------+
| **Parameters** | | **model : object, optional (default=sklearn.linear_model.LinearRegression)**    |
|                | |   The regression model which will be used for predict uplift.                   |
+----------------+-----------------------------------------------------------------------------------+


*******
Methods
*******
+-------------------------------------------------+--------------------------------------------------+
| :ref:`fit(self, X, y, t) <cadit_fit>`           | Build a model from the training set (X, y, t).   |
+-------------------------------------------------+--------------------------------------------------+
| :ref:`predict(self, X, t=None) <cadit_predict>` | Predict an uplift for X.                         |
+-------------------------------------------------+--------------------------------------------------+

.. _cadit_fit:

fit(self, X, y, t)
------------------
Build a model from the training set (X, y, t).

+------------------+---------------------------------------------------------------------------------+
| **Parameters**   | | **X: numpy ndarray with shape = [n_samples, n_features]**                     |
|                  | |   Matrix of features.                                                         |
|                  | | **y: numpy array with shape = [n_samples,]**                                  |
|                  | |   Array of target of feature.                                                 |
|                  | | **t: numpy array with shape = [n_samples,]**                                  |
|                  | |   Array of treatments.                                                        |
+------------------+---------------------------------------------------------------------------------+
| **Returns**      | **self : object**                                                               |
+------------------+---------------------------------------------------------------------------------+

.. _cadit_predict:

predict(self, X, t=None)
------------------------
Predict an uplift for X. 

+------------------+---------------------------------------------------------------------------------+
| **Parameters**   | | **X: numpy ndarray with shape = [n_samples, n_features]**                     |
|                  | |   Matrix of features.                                                         |
|                  | | **t: numpy array with shape = [n_samples,] or None**                          |
|                  | |   Array of treatments.                                                        |
+------------------+---------------------------------------------------------------------------------+
| **Returns**      | | **self : object**                                                             |
|                  | |   The predicted values.                                                       |
+------------------+---------------------------------------------------------------------------------+

**********
References
**********
1. Weisberg HI, Pontes VP. Post hoc subgroups in clinical trials: Anathema or analytics? // Clinical trials. 2015 Aug;12(4):357-64.

.. code-block:: python3

   from pyuplift.variable_selection import Cadit
   ...
   model = Cadit()
   model.fit(X[train_indexes, :], y[train_indexes], t[train_indexes])
   uplift = model.predict(X[test_indexes, :])
   print(uplift)
 