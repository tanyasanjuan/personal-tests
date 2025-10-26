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

# Calculate the Mode, and replace the values whit it.
# Mode = the value that appears most frequently.
x = df["Calories"].mode()[0]
df.fillna({"Calories":x}, inplace=True)
print(df.to_string)
# Results: in row 18 and 28, the empty value from "Calories" was replaced with the mode: 300.0
"""
# Data of Wromg Format
# Cells with wrong format make difficult to analyze data
# To fix it, we have two options: 
# remove the rows, or convert all cells in the columns into the same format.

# In the Data Frame, we have two cells with the wrong format. 
# Row 22 and 26, the 'Date' column should be a string that represents a date:
# Row 22: NaN, row 26: 20201226

# Convert the cells in the 'Date' column into dates.
# Pandas has a 'to_datetime()' method:
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())
# Result, the date in row 26 was fixed, but the empty date in row 22 got a NaT (Not a Time) value, 
# in other words an empty value. One way to deal with empty values is simply removing the entire row.

# Removing rows
# NaT value, can be handled as a NULL value,
# and we can remove the row by using the dropna() method.

df.dropna(subset=['Date'], inplace=True)
print(df.to_string)

# Fixing wrong data
# "Wrong data" does not have to be "empty cells" or "wrong format", 
# it can just be wrong, like if someone registered "199" instead of "1.99".
# in the dataset in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.
# taking in consideration that this is the data set of someone's workout sessions, 
# we conclude with the fact that this person did not work out in 450 minutes.

# One way to fix wrong values is to replace them
# in the dataset can be a typo error.
df.loc[7, 'Duration'] = 45
print(df.to_string())
