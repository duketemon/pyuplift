import pandas as pd
from statistics import mean


def get_average_effect(y_test, t_test, y_pred, test_share=0.3):
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
    return mean(s1) - mean(s0)
