##############################
load_hillstrom_email_marketing
##############################

Loading the Hillstrom Email Marketing dataset from the local file.

****************
Data description
****************
This dataset contains 64,000 customers who last purchased within twelve months. The customers were involved in an e-mail test.

 * 1/3 were randomly chosen to receive an e-mail campaign featuring Mens merchandise.
 * 1/3 were randomly chosen to receive an e-mail campaign featuring Womens merchandise.
 * 1/3 were randomly chosen to not receive an e-mail campaign.

During a period of two weeks following the e-mail campaign, results were tracked. Your job is to tell the world if the Mens or Womens e-mail campaign was successful.

+--------------------------+------------+
| Features                 |          8 |
+--------------------------+------------+
| Treatment                |          3 |
+--------------------------+------------+
| Samples total            |     64,000 |
+--------------------------+------------+
| Average spend rate       |    1.05091 |
+--------------------------+------------+
| Average visit rate       |    0.14678 |
+--------------------------+------------+
| Average conversion rate  |    0.00903 |
+--------------------------+------------+

More information about dataset you can find in the `official paper <http://minethatdata.com/Stochastic_Solutions_E-Mail_Challenge_2008.04.30.pdf>`_.

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
|                 | | **dataset.data**: numpy ndarray of shape (64000, 8)                                                                                  |
|                 | |   Each row corresponding to the 8 feature values in order.                                                                           |
|                 | | **dataset.feature_names**: list, size 8                                                                                              |
|                 | |   List of feature names.                                                                                                             |
|                 | | **dataset.treatment**: numpy ndarray, shape (64000,)                                                                                 |
|                 | |   Each value corresponds to the treatment.                                                                                           |
|                 | | **dataset.target**: numpy array of shape (64000,)                                                                                    |
|                 | |   Each value corresponds to one of the outcomes. By default, it's `spend` outcome (look at `target_spend` below).                    |
|                 | | **dataset.target_spend**: numpy array of shape (64000,)                                                                              |
|                 | |   Each value corresponds to how much customers spent during a two-week outcome period.                                               |
|                 | | **dataset.target_visit**: numpy array of shape (64000,)                                                                              |
|                 | |   Each value corresponds to whether people visited the site during a two-week outcome period.                                        |
|                 | | **dataset.target_conversion**: numpy array of shape (64000,)                                                                         |
|                 | |   Each value corresponds to whether they purchased at the site (“conversion”) during a two-week outcome period.                      |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+

********
Examples
********

.. code-block:: python3

   from pyuplift.datasets import load_hillstrom_email_marketing
   df = load_hillstrom_email_marketing()
   print(df)
