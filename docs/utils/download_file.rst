#############
download_file
#############

Download file from `url` to `output_path`.

+-----------------+--------------------------------------+
| **Parameters**  | | **url: string**                    |
|                 | |   Data's URL.                      |
|                 | | **output_path: string**            |
|                 | |   Path where file will be saved.   |
+-----------------+--------------------------------------+
| **Returns**     | **None**                             |
+-----------------+--------------------------------------+

********
Examples
********

.. code-block:: python3

   from pyuplift.utils import download_file
   ...
    if not os.path.exists(data_path):
        if not os.path.exists(archive_path):
            download_file(url, archive_path)
