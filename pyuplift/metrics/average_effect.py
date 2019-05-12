import pandas as pd
from statistics import mean


def get_average_effect(y_test, t_test, y_pred, test_share=0.3):
    """Estimating an average effect of the test set.

    +-----------------+----------------------------------------------------------------------------------+
    | **Parameters:** | | **y_test**: numpy array                                                        |
    |                 | |   Actual y values.                                                             |
    |                 | | **t_test**: numpy array                                                        |
    |                 | |   Actual treatment values.                                                     |
    |                 | | **y_pred**: numpy array                                                        |
    |                 | |   Predicted y values by uplift model.                                          |
    |                 | | **test_share**: float                                                          |
    |                 | |   Share of the test data which will be taken for estimating an average effect. |
    +-----------------+----------------------------------------------------------------------------------+
    | **Returns:**    | | **average effect**: float                                                      |
    |                 | |   Average effect on the test set.                                              |
    +-----------------+----------------------------------------------------------------------------------+

    ********
    Examples
    ********

    .. code-block:: python3

       from pyuplift.metrics import get_average_effect
       ...
       train_indexes, test_indexes = train_test_split_indexes(y, train_share, seed)
       model.fit(X[train_indexes, :], y[train_indexes], t[train_indexes])
       effect = get_average_effect(
              y[test_indexes],
              t[test_indexes],
              model.predict(X[test_indexes, :])
       )
       print(effect)
    """

    df = pd.DataFrame(data={
        'effect': y_pred,
        'y': y_test,
        't': t_test
    })
    df = df.sort_values(by='effect', ascending=False)
    test_size = int(test_share * df.shape[0])
    idx, s1, s0 = 0, [], []
    for _, row in df.iterrows():
        if idx > test_size:
            break
        if row['t'] == 1:
            s1.append(row['y'])
        else:
            s0.append(row['y'])
        idx += 1
    if len(s0) == 0:
        s0.append(0)
    if len(s1) == 0:
        s1.append(0)
    return mean(s1) - mean(s0)
