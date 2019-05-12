import os
import requests


def download_file(url: str, output_path: str):
    """Download file from `url` to `output_path`.

    +-----------------+--------------------------------------+
    | **Parameters**  | | **url: string**                    |
    |                 | |   Data's URL.                      |
    |                 | | **output_path: string**            |
    |                 | |   Path where file will be saved.   |
    +-----------------+--------------------------------------+
    | **Returns**     | **None**                             |
    +-----------------+--------------------------------------+
    """
    if not os.path.isfile(output_path):
        print("Downloading file to '{}'...".format(output_path))
        response = requests.get(url)
        # Check if the response is ok (200)
        if response.status_code == 200:
            # Open file and write the content
            with open(output_path, 'wb') as file:
                # A chunk of 128 bytes
                for chunk in response:
                    file.write(chunk)
