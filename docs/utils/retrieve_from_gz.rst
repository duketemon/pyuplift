################
retrieve_from_gz
################

The retrieving gz-archived data from `archive_path` to `output_path`.

+-----------------+--------------------------------------+
| **Parameters**  | | **archive_path: string**           |
|                 | |   The archive path.                |
|                 | | **output_path: string**            |
|                 | |   The retrieved data path.         |
+-----------------+--------------------------------------+
| **Returns**     | **None**                             |
+-----------------+--------------------------------------+

********
Examples
********

.. code-block:: python3

   from pyuplift.utils import retrieve_from_gz
   ...
    if not os.path.exists(data_path):
        if not os.path.exists(archive_path):
            download_file(url, archive_path)
		retrieve_from_gz(archive_path, data_path)
