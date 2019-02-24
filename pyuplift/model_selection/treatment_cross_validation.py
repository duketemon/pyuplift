import numpy as np
import pandas as pd
from statistics import mean


def treatment_cross_val_score(x, y, t, model, cv=5, test_share=0.3):
    """Evaluate a scores by cross-validation

    Parameters
    ----------
    x : numpy array of shape = [n_samples, n_features]
        The training input samples.
    y : numpy array of shape = [n_samples] or [n_samples, n_outputs]
        The target values (class labels in classification, real numbers in regression).
    t : numpy array of shape = [n_samples] or [n_samples, n_outputs]
        The treatments.
    model : Derived class of the BaseModel
        The model of predicting treatment effect.
    cv : int, default: 5
         The number of splits.
    test_share : callable, default: 0.3
        The ``test_share`` should be between 0.0 and 1.0 and represent the
        proportion of the dataset to predict effect.
    Returns
    -------
    scores : numpy array of floats
    """
    steps = [0] * cv
    for i in range(len(y)):
        steps[i % cv] += 1
    ind = 0
    scores = []
    for i in range(cv):
        x_train = np.concatenate((x[:ind, :], x[ind + steps[i]:, :]), axis=0)
        y_train = np.append(y[:ind], y[ind + steps[i]:])
        t_train = np.append(t[:ind], t[ind + steps[i]:])
        model.fit(x_train, y_train, t_train)

        x_test = x[ind:ind + steps[i], :]
        y_test = y[ind:ind + steps[i]]
        t_test = t[ind:ind + steps[i]]
        y_pred = model.predict(x_test)

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
        scores.append(mean(s1) - mean(s0))

        ind += steps[i]
    return np.array(scores)
