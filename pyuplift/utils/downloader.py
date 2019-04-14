import os
import requests


def download_file(url: str, path: str):
    """The downloading file from `url` and saving to `path`.

    Parameters
    ----------
    url : str
        The URL to file with data.
    path : str
        The saving path.
    """
    if not os.path.isfile(path):
        print("Downloading file to '{}'...".format(path))
        response = requests.get(url)
        # Check if the response is ok (200)
        if response.status_code == 200:
            # Open file and write the content
            with open(path, 'wb') as file:
                # A chunk of 128 bytes
                for chunk in response:
                    file.write(chunk)
