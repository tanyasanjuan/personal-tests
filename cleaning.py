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

