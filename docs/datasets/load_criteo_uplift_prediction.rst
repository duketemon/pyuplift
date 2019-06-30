#############################
load_criteo_uplift_prediction
#############################

Loading the Criteo Uplift Prediction dataset from the local file.

****************
Data description
****************
This dataset is constructed by assembling data resulting from several incrementality tests, a particular randomized trial procedure where a random part of the population is prevented from being targeted by advertising.
It consists of 25M rows, each one representing a user with 11 features, a treatment indicator and 2 labels (visits and conversions).

*******
Privacy
*******
For privacy reasons the data has been sub-sampled non-uniformly so that the original incrementality level cannot be deduced from the dataset while preserving a realistic, challenging benchmark.
Feature names have been anonymized and their values randomly projected so as to keep predictive power while making it practically impossible to recover the original features or user context.

+--------------------------+------------+
| Features                 |         11 |
+--------------------------+------------+
| Treatment                |          2 |
+--------------------------+------------+ 
| Samples total            | 25,309,483 |
+--------------------------+------------+ 
| Average visit rate       |    0.04132 |
+--------------------------+------------+ 
| Average conversion rate  |    0.00229 |
+--------------------------+------------+

More information about dataset you can find in
the `official dataset description <http://ailab.criteo.com/criteo-uplift-prediction-dataset>`_.

+-----------------+---------------------------------------------------------------------------------------------------------------------+
| **Parameters**  | | **data_home: str**                                                                                                |
|                 | |   Specify another download and cache folder for the dataset.                                                      |
|                 | |   By default the dataset will be stored in the data folder in the same folder.                                    |
|                 | | **download_if_missing: bool, default=True**                                                                       |
|                 | |   Download the dataset if it is not downloaded.                                                                   |
+-----------------+---------------------------------------------------------------------------------------------------------------------+
| **Returns:**    | | **dataset**: dict                                                                                                 |
|                 | |   Dictionary object with the following attributes:                                                                |
|                 | | **dataset.description** : str                                                                                     |
|                 | |   Description of the Criteo Uplift Prediction dataset.                                                            |
|                 | | **dataset.data**: numpy ndarray of shape (25309483, 11)                                                           |
|                 | |   Each row corresponding to the 11 feature values in order.                                                       |
|                 | | **dataset.feature_names**: list, size 11                                                                          |
|                 | |   List of feature names.                                                                                          |
|                 | | **dataset.treatment**: numpy ndarray, shape (25309483,)                                                           |
|                 | |   Each value corresponds to the treatment.                                                                        |
|                 | | **dataset.target**: numpy array of shape (25309483,)                                                              |
|                 | |   Each value corresponds to one of the outcomes. By default, it's `visit` outcome (look at `target_visit` below). |
|                 | | **dataset.target_visit**: numpy array of shape (25309483,)                                                        |
|                 | |   Each value corresponds to whether a visit occurred for this user (binary, label).                               |
|                 | | **dataset.target_exposure**: numpy array of shape (25309483,)                                                     |
|                 | |   Each value corresponds to treatment effect, whether the user has been effectively exposed (binary).             |
|                 | | **dataset.target_conversion**: numpy array of shape (25309483,)                                                   |
|                 | |   Each value corresponds to whether a conversion occurred for this user (binary, label).                          |
+-----------------+---------------------------------------------------------------------------------------------------------------------+

********
Examples
********

.. code-block:: python3

   from pyuplift.datasets import load_criteo_uplift_prediction
   df = load_criteo_uplift_prediction()
   print(df)
