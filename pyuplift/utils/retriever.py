import gzip
import shutil


def retrieve_from_gz(archive_path, data_path):
    """The retrieving gz-archived data from `archive_path` to `data_path`.

    Parameters
    ----------
    archive_path : str
        The archive path.
    data_path : str
        The retrieved data path.
    """
    with gzip.open(archive_path, 'rb') as f_in:
        with open(data_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
