from pyuplift.variable_selection import Dummy
from pyuplift.model_selection import train_test_split
from pyuplift.datasets import make_linear_regression
from pyuplift.metrics import get_average_effect


random_state = 123
df = make_linear_regression(10000)
X, y, t = df.drop(['y', 't'], axis=1).values, df['y'].values, df['t'].values
X_train, X_test, y_train, y_test, t_train, t_test = train_test_split(X, y, t, random_state=random_state)

model = Dummy()
model.fit(X_train, y_train, t_train)


def test_get_average_effect__zero_test_share():
    y_pred = model.predict(X_test)
    test_share = 0
    effect = get_average_effect(y_test, t_test, y_pred, test_share)
    assert effect == 0
