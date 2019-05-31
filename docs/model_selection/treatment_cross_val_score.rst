#########################
treatment_cross_val_score
#########################

Evaluate a scores by cross-validation.

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

********
Examples
********

.. code-block:: python3

   from pyuplift.model_selection import treatment_cross_val_score
   ...
   for model_name in models:
       scores = treatment_cross_val_score(X, y, t, models[model_name], cv, seeds=seeds)
