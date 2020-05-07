#"Generate more data" function, takes dataframes and makes more rows
import pandas as pd
import numpy as np
#pick how many rows
#n = (input("How many new rows?"))
def more_data_func(n, df):
    #first, add 'n' new rows with null values
    #for _ in range(n):
    #    df.loc[df.iloc[-1].name + 1,:] = np.nan
    #for each column, check data type
    columns = list(df)
    x_vals = []
    for _ in range(n):
        for i in columns:
            if [(df[i].dtype) != int]:
                x = df[i].mode('columns')
            elif [(df[i].dtype) == int]:
                x = df[i].mean()
            else:
                x=np.nan
            x_vals.append(x)
        df2 = pd.DataFrame([x_vals])
        df.append(df2)
    print(df)
    #if number, new row has average
    #if category, new row has median
