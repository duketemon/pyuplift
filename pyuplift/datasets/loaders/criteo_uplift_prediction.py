import os
import pandas as pd
from pyuplift.utils import download_file, retrieve_from_gz


def load_criteo_uplift_prediction(
        url='https://s3.us-east-2.amazonaws.com/criteo-uplift-dataset/criteo-uplift.csv.gz',
):
    """Load and return the Criteo Uplift Prediction dataset.

    ****************
    Data description
    ****************
    This dataset is constructed by assembling data resulting from several incrementality tests, a particular randomized trial procedure where a random part of the population is prevented from being targeted by advertising.
    It consists of 25M rows, each one representing a user with 11 features, a treatment indicator and 2 labels (visits and conversions).

    *******
    Privacy
    *******
    For privacy reasons the data has been sub-sampled non-uniformly so that the original incrementality level cannot be deduced from the dataset while preserving a realistic, challenging benchmark.
    Feature names have been anonymized and their values randomly projected so as to keep predictive power while making it practically impossible to recover the original features or user context.

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
    url : str
        The URL to file with data.

    Returns
    -------
    dataset : dict object with the following attributes:

    dataset.DESCR : str
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

    folder_path = os.path.join(os.sep.join(__file__.split(os.sep)[:-1]), 'data')
    filename = 'criteo_uplift_prediction'
    archive_path = os.path.join(folder_path, filename + '.gz')
    data_path = os.path.join(folder_path, filename + '.csv')
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)

    if not os.path.exists(data_path):
        if not os.path.exists(archive_path):
            download_file(url, archive_path)
        retrieve_from_gz(archive_path, data_path)

    df = pd.read_csv(data_path)
    description = 'This dataset is constructed by assembling data resulting from several incrementality tests, ' \
                  'a particular randomized trial procedure where a random part of the population' \
                  'is prevented from being targeted by advertising. It consists of 25M rows, ' \
                  'each one representing a user with 11 features, a treatment indicator and ' \
                  '2 labels (visits and conversions).'
    dataset = {
        'DESCR': description,
        'data': df.drop(['exposure', 'visit', 'conversion', 'treatment'], axis=1).values,
        'feature_names': list(filter(lambda x: x not in ['exposure', 'visit', 'conversion', 'treatment'], df.columns)),
        'treatment': df['treatment'].values,
        'target': df['visit'].values,
        'target_visit': df['visit'].values,
        'target_exposure': df['exposure'].values,
        'target_conversion': df['conversion'].values,
    }
    return dataset
