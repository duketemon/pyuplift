import os
import numpy as np
import pandas as pd
from pyuplift.utils import download_file, retrieve_from_gz


def download_criteo_uplift_prediction(
    data_home=None,
    url='https://s3.us-east-2.amazonaws.com/criteo-uplift-dataset/criteo-uplift.csv.gz'
):
    """Downloading the Criteo Uplift Prediction dataset.

    ****************
    Data description
    ****************
    This dataset is constructed by assembling data resulting from several incrementality tests,
    a particular randomized trial procedure
    where a random part of the population is prevented from being targeted by advertising.
    It consists of 25M rows, each one representing a user with 11 features,
    a treatment indicator and 2 labels (visits and conversions).

    *******
    Privacy
    *******
    For privacy reasons the data has been sub-sampled non-uniformly so that the original incrementality level
    cannot be deduced from the dataset while preserving a realistic, challenging benchmark.
    Feature names have been anonymized and their values randomly projected so as to keep predictive power
    while making it practically impossible to recover the original features or user context.

    +--------------------------+------------+
    |Features                  |         11 |
    +--------------------------+------------+
    |Treatment                 |          2 |
    +--------------------------+------------+
    |Samples total             | 25,309,483 |
    +--------------------------+------------+
    |Average visit rate        |    0.04132 |
    +--------------------------+------------+
    |Average conversion rate   |    0.00229 |
    +--------------------------+------------+

    More information about dataset you can find in
    the `official dataset description <http://ailab.criteo.com/criteo-uplift-prediction-dataset>`_.

    +-----------------+----------------------------------------------------------------------------------+
    | **Parameters**  | | **data_home: string**                                                          |
    |                 | |   Specify another download and cache folder for the dataset.                   |
    |                 | |   By default the dataset will be stored in the data folder in the same folder. |
    |                 | | **url: string**                                                                |
    |                 | |   The URL to file with data.                                                   |
    +-----------------+----------------------------------------------------------------------------------+
    | **Returns**     | **None**                                                                         |
    +-----------------+----------------------------------------------------------------------------------+
    """

    data_home, dataset_path = __get_data_home_dataset_file_paths(data_home)
    if not os.path.isdir(data_home):
        os.makedirs(data_home)

    archive_path = dataset_path.replace('.csv', '.gz')
    if not os.path.exists(dataset_path):
        if not os.path.exists(archive_path):
            download_file(url, archive_path)
        retrieve_from_gz(archive_path, dataset_path)


def load_criteo_uplift_prediction(
    data_home=None,
    download_if_missing=True
):
    """Loading the Criteo Uplift Prediction dataset from the local file.

    ****************
    Data description
    ****************
    This dataset is constructed by assembling data resulting from several incrementality tests,
    a particular randomized trial procedure
    where a random part of the population is prevented from being targeted by advertising.
    It consists of 25M rows, each one representing a user with 11 features,
    a treatment indicator and 2 labels (visits and conversions).

    *******
    Privacy
    *******
    For privacy reasons the data has been sub-sampled non-uniformly so that the original incrementality level
    cannot be deduced from the dataset while preserving a realistic, challenging benchmark.
    Feature names have been anonymized and their values randomly projected so as to keep predictive power
    while making it practically impossible to recover the original features or user context.

    +--------------------------+------------+
    |Features                  |         11 |
    +--------------------------+------------+
    |Treatment                 |          2 |
    +--------------------------+------------+
    |Samples total             | 25,309,483 |
    +--------------------------+------------+
    |Average visit rate        |    0.04132 |
    +--------------------------+------------+
    |Average conversion rate   |    0.00229 |
    +--------------------------+------------+

    More information about dataset you can find in
    the `official dataset description <http://ailab.criteo.com/criteo-uplift-prediction-dataset>`_.

    Parameters
    ----------
    data_home : str, optional (default=None)
        Specify another download and cache folder for the dataset.
        By default the dataset will be stored in the data folder in the same folder.
    download_if_missing : bool, optional (default=True)
        Download the dataset if it is not downloaded.

    Returns
    -------
    dataset : dict object with the following attributes:

    dataset.description : str
        Description of the Criteo Uplift Prediction dataset.

    dataset.data : ndarray, shape (25309483, 11)
        Each row corresponding to the 11 feature values in order.

    dataset.feature_names : list, size 11
        List of feature names.

    dataset.treatment : ndarray, shape (25309483,)
        Each value corresponds to the treatment.

    dataset.target : numpy array of shape (25309483,)
        Each value corresponds to one of the outcomes. By default, it's `visit` outcome (look at `target_visit` below).

    dataset.target_visit : numpy array of shape (25309483,)
        Each value corresponds to whether a visit occurred for this user (binary, label).

    dataset.target_exposure : numpy array of shape (25309483,)
        Each value corresponds to treatment effect, whether the user has been effectively exposed (binary).

    dataset.target_conversion : numpy array of shape (25309483,)
        Each value corresponds to whether a conversion occurred for this user (binary, label).
    """

    data_home, dataset_path = __get_data_home_dataset_file_paths(data_home)
    if not os.path.exists(dataset_path):
        if download_if_missing:
            download_criteo_uplift_prediction(data_home)
        else:
            raise FileNotFoundError(
                'The dataset does not exist. '
                'Use `download_criteo_uplift_prediction` function to download the dataset.'
            )

    df = pd.read_csv(dataset_path)
    description = 'This dataset is constructed by assembling data resulting from several incrementality tests, ' \
                  'a particular randomized trial procedure where a random part of the population' \
                  'is prevented from being targeted by advertising. It consists of 25M rows, ' \
                  'each one representing a user with 11 features, a treatment indicator and ' \
                  '2 labels (visits and conversions).'

    drop_names = ['exposure', 'visit', 'conversion', 'treatment']
    dataset = {
        'description': description,
        'data': df.drop(drop_names, axis=1).values,
        'feature_names': np.array([name for name in df.columns if name not in drop_names]),
        'treatment': df['treatment'].values,
        'target': df['visit'].values,
        'target_visit': df['visit'].values,
        'target_exposure': df['exposure'].values,
        'target_conversion': df['conversion'].values,
    }
    return dataset


def __get_data_home_dataset_file_paths(data_home_path):
    if data_home_path is None:
        data_home_path = os.path.join(os.sep.join(__file__.split(os.sep)[:-1]), 'data')
    dataset_path = os.path.join(data_home_path, 'criteo_uplift_prediction.csv')
    return data_home_path, dataset_path


