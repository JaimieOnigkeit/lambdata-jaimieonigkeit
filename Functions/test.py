import pandas as pd
from pandas import DataFrame
import numpy as np
from more_data import more_data_func

df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["x", "x", "z"]})
more_data_func(df)

# print(df)
