import os
import shutil
import pytest
from pyuplift.datasets import load_criteo_uplift_prediction
from pyuplift.datasets import download_criteo_uplift_prediction


data_home = os.path.join(os.sep.join(__file__.split(os.sep)[:-1]), 'data')


def test_load_criteo_uplift_prediction__do_not_download_if_missing():
    with pytest.raises(FileNotFoundError):
        load_criteo_uplift_prediction(data_home=data_home, download_if_missing=False)


def test_download_criteo_uplift_prediction__wrong_url():
    with pytest.raises(Exception):
        download_criteo_uplift_prediction(url='https://s3.us-east-2.amazonaws.com/criteo-uplift/criteo-uplift.csv.gz')


def test_download_criteo_uplift_prediction():
    download_criteo_uplift_prediction(data_home=data_home)
    # shutil.rmtree(data_home)


def test_load_criteo_uplift_prediction():
    df = load_criteo_uplift_prediction(data_home=data_home)
    assert len(df['feature_names']) != 11
    shutil.rmtree(data_home)
