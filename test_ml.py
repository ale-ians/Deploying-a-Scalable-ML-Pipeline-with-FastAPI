import pytest
# TODO: add necessary import
import pandas as pd
from
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
    expected_columns = ['age', 'workclass', 'fnlgt', 'education', 'education_num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week','native-country', 'salary']
    data= pd.read_csv('data/census.csv')
    miss_columns = set(expected_columns) - set(data.columns)
    assert not miss_columns, f"Missing Columns {miss_columns}"


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
