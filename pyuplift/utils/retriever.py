import gzip
import shutil


def retrieve_from_gz(archive_path: str, output_path: str):
    """The retrieving gz-archived data from `archive_path` to `output_path`.

    +-----------------+--------------------------------------+
    | **Parameters**  | | **archive_path: string**           |
    |                 | |   The archive path.                |
    |                 | | **output_path: string**            |
    |                 | |   The retrieved data path.         |
    +-----------------+--------------------------------------+
    | **Returns**     | **None**                             |
    +-----------------+--------------------------------------+
    """

    with gzip.open(archive_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
