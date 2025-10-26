# Pandas is a Python libraty, works to work with data sets.
# it has functions for analizyng, cleanin, exploring and manipulate data.
# Pandas refers to 'Panel Data' and 'Python Data Analysis'
# 'pd' is the alias of Pandas, we can import an alias with the keyword 'as'
# after name the alias, pandas ca be referred to as 'pd' instead o 'pandas'
# Source of Pandas' code: https://github.com/pandas-dev/pandas
# This program loads a CVS file into a pandas DataFrame


# import pandas
import pandas as pd

# check the version of pandas. Result 2.2.2
# print(pd.__version__)

# Series
# Pandas series is like a column in a table, it's a one-dimensional array holding data.
# Each item in the list becomes a value in the Series, 
# and pandas automatically assigns it an index (by default, it starts at 0).


# create a simple pandas Series from a list:
lista = [1,7,2]
mivariable = pd.Series(lista)
print(mivariable)
# Results: 'list and dtype: int64'
# 'dtype: int64': Indicates that the values ​​are of 64-bit integer type.


# Labels
# If nothing else is specdied, the values are labeled with their index number. 
# First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value.
print(mivariable[1])

# with the 'index' argument, we can name our own labels.
mivariable = pd.Series(lista, index = ['x', 'y', 'z'])
print(mivariable)
# results, instead to print the index (0, 1, 2) will print (x, y, z)
# we can access an item by referring to the label.
print(mivariable['z'])

#df = pd.read_csv('dataprueba.csv')
#print(df.to_string())