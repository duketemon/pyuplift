import os
import shutil
import pytest
from pyuplift.datasets import download_hillstrom_email_marketing


data_home = os.path.join(os.sep.join(__file__.split(os.sep)[:-1]), 'data')


def test_download_hillstrom_email_marketing():
    download_hillstrom_email_marketing(data_home=data_home)
    shutil.rmtree(data_home)


def test_download_hillstrom_email_marketing__twice():
    download_hillstrom_email_marketing(data_home=data_home)
    download_hillstrom_email_marketing(data_home=data_home)
    shutil.rmtree(data_home)


def test_download_hillstrom_email_marketing__wrong_url():
    with pytest.raises(Exception):
        download_hillstrom_email_marketing(url='http://www.minethatdata.com/Kevin_Hillstrom_Min')
