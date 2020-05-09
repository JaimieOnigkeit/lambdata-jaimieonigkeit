# "Generate more data" function, takes dataframes and makes more rows
import pandas as pd
import numpy as np
#df = DataFrame({"a":[1,2,3], "b":[4,5,6], "c":["x", "x", "z"]})


def more_data_func(df):
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
