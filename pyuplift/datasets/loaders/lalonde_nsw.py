import os
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
    column_types=column_types
):

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
        df = shuffle(df)
        df.to_csv(dataset_path, index=False)


def __get_data_home_dataset_file_paths(data_home_path):
    if data_home_path is None:
        data_home_path = os.path.join(os.sep.join(__file__.split(os.sep)[:-1]), 'data')
    dataset_path = os.path.join(data_home_path, 'lalonde_nsw.csv')
    return data_home_path, dataset_path

