#####
Dummy
#####

The class which implements the dummy approach [1].

+----------------+-----------------------------------------------------------------------------------+
| **Parameters** | | **model : object, optional (default=sklearn.linear_model.LinearRegression)**    |
|                | |   The regression model which will be used for predict uplift.                   |
+----------------+-----------------------------------------------------------------------------------+


*******
Methods
*******
+-------------------------------------------------+-----------------------------------------------------+
| :ref:`fit(self, X, y, t) <dummy_fit>`           | Build a dummy model from the training set (X, y, t).|
+-------------------------------------------------+-----------------------------------------------------+
| :ref:`predict(self, X, t=None) <dummy_predict>` | Predict an uplift for X.                            |
+-------------------------------------------------+-----------------------------------------------------+

.. _dummy_fit:

fit(self, X, y, t)
------------------
Build a dummy model from the training set (X, y, t).

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

.. _dummy_predict:

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
1. A Literature Survey and Experimental Evaluation of the State-of-the-Art in Uplift Modeling: A Stepping Stone Toward the Development of Prescriptive Analytics by Floris Devriendt, Darie Moldovan, and Wouter Verbeke


.. code-block:: python3

   from pyuplift.variable_selection import Dummy
   ...
   model = Dummy()
   model.fit(X[train_indexes, :], y[train_indexes], t[train_indexes])
   uplift = model.predict(X[test_indexes, :])
   print(uplift)
 