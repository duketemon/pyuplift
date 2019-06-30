####################
download_lalonde_nsw
####################

Downloading the Lalonde NSW dataset.

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

+-----------------+----------------------------------------------------------------------------------+
| **Parameters**  | | **data_home: str**                                                             |
|                 | |   Specify another download and cache folder for the dataset.                   |
|                 | |   By default the dataset will be stored in the data folder in the same folder. |
|                 | | **control_data_url: str**                                                      |
|                 | |   The URL to file with data of the control group.                              |
|                 | | **treated_data_url: str**                                                      |
|                 | |   The URL to file with data of the treated group.                              |
|                 | | **separator: str**                                                             |
|                 | |   The separator which used in the data files.                                  |
|                 | | **column_names: list**                                                         |
|                 | |   List of column names of the dataset.                                         |
|                 | | **column_types: dict**                                                         |
|                 | |   List of types for columns of the dataset.                                    |
|                 | | **random_state: int**                                                          |
|                 | |   The random seed.                                                             |
+-----------------+----------------------------------------------------------------------------------+
| **Returns**     | **None**                                                                         |
+-----------------+----------------------------------------------------------------------------------+


********
Examples
********

.. code-block:: python3

   from pyuplift.datasets import download_lalonde_nsw
   download_lalonde_nsw()
