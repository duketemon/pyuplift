import os
import pytest
from pyuplift.utils import download_file


def test_download_file__success():
    url = 'https://github.com/duketemon/pyuplift/blob/master/LICENSE'
    output = 'LICENSE'
    download_file(url, output)
    os.remove(output)


def test_download_file__exist_file():
    output = 'exist_file_test.test'
    with open(output, 'w') as f:
        f.write('test')
    url = 'https://github.com/duketemon/pyuplift/blob/master/LICENSE'
    download_file(url, output)
    os.remove(output)


def test_download_file__wrong_url():
    output = 'LICENSE12'
    url = 'https://githu404b.com/duketemon/pyuplift/blob/master/LICENSE'
    with pytest.raises(Exception):
        download_file(url, output)


def test_download_file__wrong_output_path():
    output = '/data23/LICENSE'
    url = 'https://github.com/duketemon/pyuplift/blob/master/LICENSE'
    with pytest.raises(FileNotFoundError):
        download_file(url, output)
