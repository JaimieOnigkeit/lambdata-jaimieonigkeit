# Single function to take a list, turn it into a series
# and add it to a dataframe as a new column
import pandas as pd


def list_func(df):
    # Get list
    prompt = (input("Enter the items for the new column, seperated by commas"))
    prompt_list = prompt.split(",")
    col_name = (input("Enter the column header"))
    items = []
    for i in range(len(prompt_list)):
        item = [prompt_list[i]]
        items.append(item)
    # Turn it into series
    data = pd.Series(items)
    # Add to dataframe as new column
    df[col_name] = data
    print(df)
