import os
import shutil
import pytest
from pyuplift.datasets import download_hillstrom_email_marketing
from pyuplift.datasets import load_hillstrom_email_marketing


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


def test_load_hillstrom_email_marketing__using_encoded_data():
    df = load_hillstrom_email_marketing(data_home=data_home, load_raw_data=False)
    assert len(df['feature_names']) == 18
    shutil.rmtree(data_home)


def test_load_hillstrom_email_marketing__using_raw_data():
    df = load_hillstrom_email_marketing(data_home=data_home, load_raw_data=True)
    assert len(df['feature_names']) != 18
    shutil.rmtree(data_home)


def test_load_hillstrom_email_marketing__do_not_download_if_missing():
    with pytest.raises(FileNotFoundError):
        load_hillstrom_email_marketing(data_home=data_home, download_if_missing=False)
