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
