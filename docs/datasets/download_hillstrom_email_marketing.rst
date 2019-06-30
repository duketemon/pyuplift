##################################
download_hillstrom_email_marketing
##################################

Downloading the Hillstrom Email Marketing dataset.

****************
Data description
****************
This dataset contains 64,000 customers who last purchased within twelve months.
The customers were involved in an e-mail test.

 * 1/3 were randomly chosen to receive an e-mail campaign featuring Mens merchandise.
 * 1/3 were randomly chosen to receive an e-mail campaign featuring Womens merchandise.
 * 1/3 were randomly chosen to not receive an e-mail campaign.

During a period of two weeks following the e-mail campaign, results were tracked.
Your job is to tell the world if the Mens or Womens e-mail campaign was successful.

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

More information about dataset you can find in
the `official paper <http://minethatdata.com/Stochastic_Solutions_E-Mail_Challenge_2008.04.30.pdf>`_.

+-----------------+----------------------------------------------------------------------------------+
| **Parameters**  | | **data_home: str**                                                             |
|                 | |   Specify another download and cache folder for the dataset.                   |
|                 | |   By default the dataset will be stored in the data folder in the same folder. |
|                 | | **url: str**                                                                   |
|                 | |   The URL to file with data.                                                   |
+-----------------+----------------------------------------------------------------------------------+
| **Returns**     | **None**                                                                         |
+-----------------+----------------------------------------------------------------------------------+

********
Examples
********

.. code-block:: python3

   from pyuplift.datasets import load_hillstrom_email_marketing
   df = load_hillstrom_email_marketing(data_home=data_home, load_raw_data=True)
   print(df)
