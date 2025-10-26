# Data Cleaning
# Means to fix bad data in the data set.
# Bad data can be: Empty cells, data in wrong format, wrong data, duplicates.
# We will use 'toclean.csc' file. 
# This data set contains empty cells ("Date" in row 22, and "Calories" in row 18 and 28).
# Wrong format ("Date" in row 26). Wrong data ("Duration" in row 7).
# Duplicates (row 11 and 12).


import pandas as pd
df = pd.read_csv('toclean.csv')
print(df)

# Empty cells, can give wrong results
# We can remove rows that cointan empy cells
# This is okay, when the dataset is not very big and remove a few rows will not have big impact.
"""
# The dropna() method returns a new DataFrame, and will not change the original.
new_df = df.dropna()
print(new_df.to_string())
# In the result that some rows have been removed (row 18, 22 and 28), because they had empty values.

# If we want to change the original DataFrame, we can use 'inplace = True' argument.
# The 'dropna(inplace = True)' will NOT return a new DataFrame, 
# but it will remove all rows containing NULL values from the original DataFrame.
df.dropna(inplace=True)
print(df.to_string())
# The result that some rows have been removed (row 18, 22 and 28), because they had empty values.


# Replace empty values. 
# Another way of dealing with empty cells is to insert a new value.
# The fillna() method allows to replace empty cells with a value:
df.fillna(130, inplace=True)
print(df.to_string())
# result: empty cells got the value 130 or 130.0 (in row 18, 22 and 28).

# Replace only for specified columns, instead to replace all empty cells in the whole DF
# We can replace, specifying the column name. 

# Replace values in the "calories" columns with the number 130
df.fillna({"Calories": 130}, inplace=True)
# Result: This operation inserts 130 in empty cells in the "Calories" column (row 18 and 28).


# Replace using mean() median() and mode()
# A way to replace empty cells, is to calculate the mean, median or mode value of the column.
x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace=True)
print(df.to_string())
# In row 18 and 28, the empty values from "Calories" was replaced with the mean: 304.68
# Mean = the average value (the sum of all values divided by number of values).

# Calculate the Median and replace the values whit it.
# Median = the value in the middle, after sorted all values ascending.
x = df["Calories"].median()
df.fillna({"Calories": x}, inplace=True)
print(df.to_string())
# row 18 and 28, the empty values from "Calories" was replaced with the median: 291.2
"""
# Calculate the Mode, and replace the values whit it.
x = df["Calories"].mode()[0]
df.fillna({"Calories":x}, inplace=True)
print(df.to_string)