import os
import shutil
import pytest
from pyuplift.utils import retrieve_from_gz


data_home = os.path.join(os.sep.join(__file__.split(os.sep)[:-1]), 'data')


def test_retrieve_from_gz():
    output_path = os.path.join(data_home, 'test.test')
    archive_path = output_path + '.gz'
    retrieve_from_gz(archive_path, output_path)
    with open(output_path, 'r') as f:
        text = f.read()
    os.remove(output_path)
    assert text == 'good'
