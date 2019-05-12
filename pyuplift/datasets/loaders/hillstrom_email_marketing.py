import os
import pandas as pd
from pyuplift.utils import download_file


def load_hillstrom_email_marketing(
        load_raw_data=False,
        url='http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv',
):
    """Load and return the Hillstrom Email Marketing dataset.

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
    url : str
        The URL to file with data.

    Returns
    -------
    dataset : dict object with the following attributes:

    dataset.DESCR : str
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

    folder_path = os.path.join(os.sep.join(__file__.split(os.sep)[:-1]), 'data')
    file_path = os.path.join(folder_path, 'hillstrom_email_marketing.csv')
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)

    if not os.path.exists(file_path):
        download_file(url, file_path)

    df = pd.read_csv(file_path)
    if not load_raw_data:
        df = __encode_data(df)

    description = 'This dataset contains 64,000 customers who last purchased within twelve months. ' \
                  'The customers were involved in an e-mail test. ' \
                  '1/3 were randomly chosen to receive an e-mail campaign featuring Mens merchandise. ' \
                  '1/3 were randomly chosen to receive an e-mail campaign featuring Womens merchandise. ' \
                  '1/3 were randomly chosen to not receive an e-mail campaign. ' \
                  'During a period of two weeks following the e-mail campaign, results were tracked. ' \
                  'Your job is to tell the world if the Mens or Womens e-mail campaign was successful.'

    data = {
        'DESCR': description,
        'data': df.drop(['spend', 'visit', 'conversion', 'segment'], axis=1).values,
        'feature_names': list(filter(lambda x: x not in ['spend', 'visit', 'conversion', 'segment'], df.columns)),
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
