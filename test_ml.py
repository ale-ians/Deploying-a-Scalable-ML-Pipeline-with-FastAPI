import pytest
# TODO: add necessary import
import pandas as pd
from sklearn.metrics import accuracy_score
from ml.model import train_model
from ml.data import process_data

# TODO: implement the first test. Change the function name and input as needed

def test_row_count():
    """
    Row count test.
    """
    data= pd.read_csv('data/census.csv')
    assert 32000 < data.shape[0] < 33000



# TODO: implement the second test. Change the function name and input as needed
def test_column_name():
    """
    ensures expected columns in dataset are present
    """
    expected_columns = ['age', 'workclass', 'fnlgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week','native-country', 'salary']
    data= pd.read_csv('data/census.csv')
    miss_columns = set(expected_columns) - set(data.columns)
    assert not miss_columns, f"Missing Columns {miss_columns}"


# TODO: implement the third test. Change the function name and input as needed
def test_model_accuracy():
    """
    Test model type matches LogisticRegression
    """
    data = pd.read_csv('data/census.csv')
    categorical_features = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
    label = 'salary'

    train = data.sample(frac=.8, random_state=42)
    test = data.drop(train.index)

    X_train, y_train, encoder, lb = process_data(
        test, categorical_features=categorical_features, label=label, training=True
    )
    X_test, y_test, _, _ = process_data(
        test, categorical_features=categorical_features, label=label, training=False, encoder=encoder, lb=lb
    )
    model = train_model(X_train, y_train)
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    assert acc > 0.2, f"Model Accuracy too low: {acc:.4f}"