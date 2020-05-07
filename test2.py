from list_to_column import list_func
import pandas as pd
from pandas import DataFrame

df = DataFrame({"a":[1,2,3], "b":[4,5,6], "c":["x", "x", "z"]})

list_func(df)
