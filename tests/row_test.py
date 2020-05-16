import unittest
from pandas import DataFrame
import pandas as pd
import numpy as np

def more_data_func(df):
    '''
    Creates new row(s) with NaNs
    params: input exisiting dataframe
    user input: number of rows to add
    output dataframe with number of empty rows added
    '''
    prompt = (input("How many new rows?"))
    n = int(prompt)
    columns = list(df)
    for _ in range(n):
        row = {}
        for col in columns:
            row[col] = [np.nan]
        df2 = pd.DataFrame(row)
        df = df.append(df2, ignore_index=True)
    print(df)
    
df = df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["x", "x", "z"]})

class TestRows(unittest.TestCase):
    '''
    Verifies that the passed in dataframe is 
    different than the returned dataframe
    '''
    def test_add(self):
        self.assertFalse(more_data_func(df),(df))


if __name__ == "__main__":
    unittest.main()
