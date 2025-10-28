# NumPy is a Python library used for working with arrays.
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called ndarray,
# it provides a lot of supporting functions that make working with ndarray very easy.
# https://github.com/numpy/numpy

# NumPy is usually imported under the np alias.

# NumPy Creating Arrays
# we can create a NumPy ndarray object using the array() function.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
#print(np.__version__)


# type(): This built-in Python function tells us the type of the object passed to it. 
# Results: shows that arr is numpy.ndarray type.
print(type(arr))

# Create an ndarray, we can pass a list, tuple or any array-like object into the array() method,
# and it will be converted into an ndarray.
# use a tuple to create a NumPy array:
arr = np.array((1, 2, 3, 4, 5))
print(arr)