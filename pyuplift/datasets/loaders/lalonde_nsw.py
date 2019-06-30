import os
import numpy as np
import pandas as pd
from sklearn.utils import shuffle


column_names = ['treat', 'age', 'educ', 'black', 'hisp', 'married', 'nodegr', 're75', 're78']
column_types = {
    'treat': 'int32',
    'age': 'int32',
    'educ': 'int32',
    'black': 'int32',
    'hisp': 'int32',
    'married': 'int32',
    'nodegr': 'int32',
}


def download_lalonde_nsw(
    data_home=None,
    control_data_url='https://users.nber.org/~rdehejia/data/nsw_control.txt',
    treated_data_url='https://users.nber.org/~rdehejia/data/nsw_treated.txt',
    separator=r'\s+',
    column_names=column_names,
    column_types=column_types,
    random_state=123
):
    """Downloading the Lalonde NSW dataset.

    ****************
    Data description
    ****************
    The dataset contains the treated and control units from the male sub-sample
    from the National Supported Work Demonstration as used by Lalonde in his paper.

    +--------------------------+------------+
    | Features                 |          7 |
    +--------------------------+------------+
    | Treatment                |          2 |
    +--------------------------+------------+
    | Samples total            |        722 |
    +--------------------------+------------+

    More information about dataset you can find `here <https://users.nber.org/~rdehejia/nswdata.html>`_.

    +-----------------+----------------------------------------------------------------------------------+
    | **Parameters**  | | **data_home: str**                                                             |
    |                 | |   Specify another download and cache folder for the dataset.                   |
    |                 | |   By default the dataset will be stored in the data folder in the same folder. |
    |                 | | **control_data_url: str**                                                      |
    |                 | |   The URL to file with data of the control group.                              |
    |                 | | **treated_data_url: str**                                                      |
    |                 | |   The URL to file with data of the treated group.                              |
    |                 | | **separator: str**                                                             |
    |                 | |   The separator which used in the data files.                                  |
    |                 | | **column_names: list**                                                         |
    |                 | |   List of column names of the dataset.                                         |
    |                 | | **column_types: dict**                                                         |
    |                 | |   List of types for columns of the dataset.                                    |
    |                 | | **random_state: int**                                                          |
    |                 | |   The random seed.                                                             |
    +-----------------+----------------------------------------------------------------------------------+
    | **Returns**     | **None**                                                                         |
    +-----------------+----------------------------------------------------------------------------------+
    """

    data_home, dataset_path = __get_data_home_dataset_file_paths(data_home)
    if not os.path.isdir(data_home):
        os.makedirs(data_home)

    if not os.path.exists(dataset_path):
        try:
            control_df = pd.read_csv(
                control_data_url,
                sep=separator,
                header=None,
                names=column_names,
                dtype=column_types
            )
        except:
            raise Exception(
                'The file with data of the control group not found. '
                'Check `control_data_url` value.'
            )

        try:
            treated_df = pd.read_csv(
                treated_data_url,
                sep=separator,
                header=None,
                names=column_names,
                dtype=column_types
            )
        except:
            raise Exception(
                'The file with data of the treated group not found. '
                'Check `treated_data_url` value.'
            )

        df = control_df.append(treated_df, ignore_index=True)
        df = shuffle(df, random_state=random_state)
        df.to_csv(dataset_path, index=False)


def load_lalonde_nsw(
    data_home=None,
    download_if_missing=True
):
    """Loading the Lalonde NSW dataset from the local file.

    ****************
    Data description
    ****************
    The dataset contains the treated and control units from the male sub-sample
    from the National Supported Work Demonstration as used by Lalonde in his paper.

    +--------------------------+------------+
    | Features                 |          7 |
    +--------------------------+------------+
    | Treatment                |          2 |
    +--------------------------+------------+
    | Samples total            |        722 |
    +--------------------------+------------+

    More information about dataset you can find `here <https://users.nber.org/~rdehejia/nswdata.html>`_.

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
        Description of the dataset.

    dataset.data : ndarray, shape (722, 7)
        Each row corresponding to the 7 feature values in order.

    dataset.feature_names : list, size 7
        List of feature names.

    dataset.treatment : ndarray, shape (722,)
        Each value corresponds to the treatment.

    dataset.target : numpy array of shape (722,)
        Each value corresponds to one of the outcomes. By default, it's `re78` outcome.
    """

    data_home, dataset_path = __get_data_home_dataset_file_paths(data_home)
    if not os.path.exists(dataset_path):
        if download_if_missing:
            download_lalonde_nsw(data_home)
        else:
            raise FileNotFoundError(
                'The dataset does not exist. '
                'Use `download_lalonde_nsw` function to download the dataset.'
            )

    df = pd.read_csv(dataset_path)
    description = 'The dataset contains the treated and control units from the male sub-sample ' \
                  'from the National Supported Work Demonstration as used by Lalonde in his paper.'

    drop_names = ['treat', 're78']
    dataset = {
        'description': description,
        'data': df.drop(drop_names, axis=1).values,
        'feature_names': np.array([name for name in df.columns if name not in drop_names]),
        'treatment': df['treat'].values,
        'target': df['re78'].values,
    }
    return dataset


def __get_data_home_dataset_file_paths(data_home_path):
    if data_home_path is None:
        data_home_path = os.path.join(os.sep.join(__file__.split(os.sep)[:-1]), 'data')
    dataset_path = os.path.join(data_home_path, 'lalonde_nsw.csv')
    return data_home_path, dataset_path
