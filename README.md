# lambdata-jaimieonigkeit
##To Install:
#TO DO

##Useage:
#my_mod
Contains enlarge function which multiplies an input number by 100

#Example
x=11
print(enlarge(x))

#list_to_column
Contains list_func function which takes an input list and adds it as a column 
to a specified dataframe
Notes: Do not include spaces when entering the inputs. 
Separate values by commas. 
Watch out for leading and trailing spaces.
It is not set up to check for the correct number of rows at this time, so check that.

#Example
df = DataFrame({"a":[1,2,3], "b":[4,5,6], "c":["x", "x", "z"]})
list_func(df)

#more_data
Contains more_data_func function which adds n number of rows to a dataframe. 
Currently configured to populate the new row with mean values for numbers, 
mode values for non-numbers, and NaNs otherwise.

#Example