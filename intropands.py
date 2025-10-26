# Pandas is a Python libraty, works to work with data sets.
# it has functions for analizyng, cleanin, exploring and manipulate data.
# Pandas refers to 'Panel Data' and 'Python Data Analysis'
# 'pd' is the alias of Pandas, we can import an alias with the keyword 'as'
# after name the alias, pandas ca be referred to as 'pd' instead o 'pandas'
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames
# Series: is like a column, a DataFrame: is the whole table.
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


# Key/Value Objects as Series
# creat a simple Pandas Series from a dictionary
# The keys of the dictionary become the labels
calorias = {"dia1": 420, "dia2": 380, "dia3":390}
mivariable = pd.Series(calorias)
print(mivariable)

# to select only one of the imtem in the dictionary, we use the 'index' argument
# and specify only the items we want to include on the Series
# create a series using only data from 'dia1 and dia2'
calorias = {"dia1": 420, "dia2": 380, "dia3": 390}
mivariable = pd.Series(calorias, index = ["dia1", "dia2"])
print(mivariable)

# DataFrame: is a 2 dimensional data structure, like dimensional awway or a table with rows and columns
# creat a DataFramce from two Series:
data = {"calorias": [420, 380, 390],
        "duracion": [50,40,45]
        }
mivariable = pd.DataFrame(data)
print(mivariable)

# Pandas use the 'loc' attribute to return one or more specified row(s)
# refer to the rown index:
print(mivariable.loc[0])

# return row 0 and 1:
# use a list of indexes:
# when using [], the result is a Pandas DataFrame
print(mivariable.loc[[0,1]])

# Named indexes
# with the index argument, we can name our indexes.
# adding list of names to give each row a name:
mivariable = pd.DataFrame(data, index = ["dia1", "dia2", "dia3"])
print(mivariable)

# Locate Named Indexes
# Use the named index in the 'loc' attribute to return the specified row(s)
# retur "dia2", referring to the named index:
print (mivariable.loc["dia2"])

#df = pd.read_csv('dataprueba.csv')
#print(df.to_string())