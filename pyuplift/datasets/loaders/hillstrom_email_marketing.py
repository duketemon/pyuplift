import os
import numpy as np
import pandas as pd
from pyuplift.utils import download_file


def download_hillstrom_email_marketing(
    data_home=None,
    url='http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv'
):
    """Downloading the Hillstrom Email Marketing dataset.

    ****************
    Data description
    ****************
    This dataset contains 64,000 customers who last purchased within twelve months.
    The customers were involved in an e-mail test.

     * 1/3 were randomly chosen to receive an e-mail campaign featuring Mens merchandise.
     * 1/3 were randomly chosen to receive an e-mail campaign featuring Womens merchandise.
     * 1/3 were randomly chosen to not receive an e-mail campaign.

    During a period of two weeks following the e-mail campaign, results were tracked.
    Your job is to tell the world if the Mens or Womens e-mail campaign was successful.

    +--------------------------+------------+
    |Features                  |          8 |
    +--------------------------+------------+
    |Treatment                 |          3 |
    +--------------------------+------------+
    |Samples total             |     64,000 |
    +--------------------------+------------+
    |Average spend rate        |    1.05091 |
    +--------------------------+------------+
    |Average visit rate        |    0.14678 |
    +--------------------------+------------+
    |Average conversion rate   |    0.00903 |
    +--------------------------+------------+

    More information about dataset you can find in
    the `official paper <http://minethatdata.com/Stochastic_Solutions_E-Mail_Challenge_2008.04.30.pdf>`_.

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

    if not os.path.exists(dataset_path):
        download_file(url, dataset_path)


def load_hillstrom_email_marketing(
    data_home=None,
    load_raw_data=False,
    download_if_missing=True
):
    """Loading the Hillstrom Email Marketing dataset from the local file.

    ****************
    Data description
    ****************
    This dataset contains 64,000 customers who last purchased within twelve months.
    The customers were involved in an e-mail test.

     * 1/3 were randomly chosen to receive an e-mail campaign featuring Mens merchandise.
     * 1/3 were randomly chosen to receive an e-mail campaign featuring Womens merchandise.
     * 1/3 were randomly chosen to not receive an e-mail campaign.

    During a period of two weeks following the e-mail campaign, results were tracked.
    Your job is to tell the world if the Mens or Womens e-mail campaign was successful.

    +--------------------------+------------+
    |Features                  |          8 |
    +--------------------------+------------+
    |Treatment                 |          3 |
    +--------------------------+------------+
    |Samples total             |     64,000 |
    +--------------------------+------------+
    |Average spend rate        |    1.05091 |
    +--------------------------+------------+
    |Average visit rate        |    0.14678 |
    +--------------------------+------------+
    |Average conversion rate   |    0.00903 |
    +--------------------------+------------+

    More information about dataset you can find in
    the `official paper <http://minethatdata.com/Stochastic_Solutions_E-Mail_Challenge_2008.04.30.pdf>`_.

    Parameters
    ----------
    load_raw_data : bool, default: False
        The loading of raw or preprocessed data?
    data_home : str, optional (default=None)
        Specify another download and cache folder for the dataset.
        By default the dataset will be stored in the data folder in the same folder.
    download_if_missing : bool, optional (default=True)
        Download the dataset if it is not downloaded.

    Returns
    -------
    dataset : dict object with the following attributes:

    dataset.description : str
        Description of the Hillstrom email marketing dataset.

    dataset.data : ndarray, shape (64000, 8)
        Each row corresponding to the 8 feature values in order.

    dataset.feature_names : list, size 8
        List of feature names.

    dataset.treatment : ndarray, shape (64000,)
        Each value corresponds to the treatment.

    dataset.target : numpy array of shape (64000,)
        Each value corresponds to one of the outcomes. By default, it's `spend` outcome (look at `target_spend` below).

    dataset.target_spend : numpy array of shape (64000,)
        Each value corresponds to how much customers spent during a two-week outcome period.

    dataset.target_visit : numpy array of shape (64000,)
        Each value corresponds to whether people visited the site during a two-week outcome period.

    dataset.target_conversion : numpy array of shape (64000,)
        Each value corresponds to whether they purchased at the site (“conversion”) during a two-week outcome period.
    """

    data_home, dataset_path = __get_data_home_dataset_file_paths(data_home)
    if not os.path.exists(dataset_path):
        if download_if_missing:
            download_hillstrom_email_marketing(data_home)
        else:
            raise FileNotFoundError(
                'The dataset does not exist. '
                'Use `download_hillstrom_email_marketing` function to download the dataset.'
            )

    df = pd.read_csv(dataset_path)
    if not load_raw_data:
        df = __encode_data(df)

    description = 'This dataset contains 64,000 customers who last purchased within twelve months. ' \
                  'The customers were involved in an e-mail test. ' \
                  '1/3 were randomly chosen to receive an e-mail campaign featuring Mens merchandise. ' \
                  '1/3 were randomly chosen to receive an e-mail campaign featuring Womens merchandise. ' \
                  '1/3 were randomly chosen to not receive an e-mail campaign. ' \
                  'During a period of two weeks following the e-mail campaign, results were tracked. ' \
                  'Your job is to tell the world if the Mens or Womens e-mail campaign was successful.'

    drop_fields = ['spend', 'visit', 'conversion', 'segment']
    data = {
        'description': description,
        'data': df.drop(drop_fields, axis=1).values,
        'feature_names': np.array(list(filter(lambda x: x not in drop_fields, df.columns))),
        'treatment': df['segment'].values,
        'target': df['spend'].values,
        'target_spend': df['spend'].values,
        'target_visit': df['visit'].values,
        'target_conversion': df['conversion'].values,
    }
    return data


def __encode_data(df):
    df['history_segment'] = df['history_segment'].apply(lambda s: s.split(') ')[1])
    col_name = 'zip_code'
    df = pd.get_dummies(df, columns=[col_name], prefix=col_name)

    col_name = 'history_segment'
    df = pd.get_dummies(df, columns=[col_name], prefix=col_name)

    col_name = 'channel'
    df = pd.get_dummies(df, columns=[col_name], prefix=col_name)

    encoder = {'No E-Mail': 0, 'Mens E-Mail': 1, 'Womens E-Mail': 2}
    df['segment'] = df['segment'].apply(lambda k: encoder[k])
    return df


def __get_data_home_dataset_file_paths(data_home_path):
    if data_home_path is None:
        data_home_path = os.path.join(os.sep.join(__file__.split(os.sep)[:-1]), 'data')
    dataset_path = os.path.join(data_home_path, 'hillstrom_email_marketing.csv')
    return data_home_path, dataset_path
