###############
Model Selection
###############

.. toctree::
  :hidden:
  
  train_test_split
  treatment_cross_val_score

The pyuplift.model_selection module includes model validation and splitter functions.

******************
Splitter Functions
******************

+--------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| `model_selection.train_test_split(X, y, t, [train_share, random_state]) <train_test_split.html>`_      | Split X, y, t into random train and test subsets. |
+--------------------------------------------------------------------------------------------------------+---------------------------------------------------+


****************
Model validation
****************
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------+
| `model_selection.treatment_cross_val_score(X, y, t, model, [cv, train_share, seeds]) <treatment_cross_val_score.html>`_ | Evaluate a scores by cross-validation. |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------+
