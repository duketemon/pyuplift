################
load_lalonde_nsw
################

Loading the Lalonde NSW dataset from the local file.

****************
Data description
****************
The dataset contains the treated and control units from the male sub-sample from the National Supported Work Demonstration as used by Lalonde in his paper.

+--------------------------+------------+
| Features                 |          7 |
+--------------------------+------------+
| Treatment                |          2 |
+--------------------------+------------+
| Samples total            |        722 |
+--------------------------+------------+

********************
Features description
********************
* **treat** - an indicator variable for treatment status.
* **age** - age in years.
* **educ** - years of schooling.
* **black** - indicator variable for blacks.
* **hisp** - indicator variable for Hispanics.
* **married** - indicator variable for martial status.
* **nodegr** - indicator variable for high school diploma.
* **re75** - real earnings in 1975.
* **re78** - real earnings in 1978.

More information about dataset you can find `here <https://users.nber.org/~rdehejia/nswdata.html>`_.

+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **Parameters:** | | **data_home**: str, default=None                                                                                                     |
|                 | |   Specify another download and cache folder for the dataset.                                                                         |
|                 | |   By default the dataset will be stored in the data folder in the same folder.                                                       |
|                 | | **load_raw_data**: bool, default=False                                                                                               |
|                 | |   The loading of raw or preprocessed data?                                                                                           |
|                 | | **download_if_missing**: bool, default=True                                                                                          |
|                 | |   Download the dataset if it is not downloaded.                                                                                      |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **Returns:**    | | **dataset**: dict                                                                                                                    |
|                 | |   Dictionary object with the following attributes:                                                                                   |
|                 | | **dataset.description** : str                                                                                                        |
|                 | |   Description of the Hillstrom email marketing dataset.                                                                              |
|                 | | **dataset.data**: numpy ndarray of shape (722, 7)                                                                                    |
|                 | |   Each row corresponding to the 7 feature values in order.                                                                           |
|                 | | **dataset.feature_names**: list, size 7                                                                                              |
|                 | |   List of feature names.                                                                                                             |
|                 | | **dataset.treatment**: numpy ndarray, shape (722,)                                                                                   |
|                 | |   Each value corresponds to the treatment.                                                                                           |
|                 | | **dataset.target**: numpy array of shape (722,)                                                                                      |
|                 | |   Each value corresponds to one of the outcomes. By default, it's `re78` outcome.                                                    |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+

********
Examples
********

.. code-block:: python3

   from pyuplift.datasets import load_lalonde_nsw
   df = load_lalonde_nsw()
   print(df)
