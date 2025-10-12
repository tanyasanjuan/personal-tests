# Boolean values
# Boolean values can only be True or False
print(10 > 9) # prints True, because 10 is greater than 9
print(10 == 9) # prints False, because 10 is not equal to 9
print(10 < 9) # prints False, because 10 is not less than 9

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# We can use the bool() function to evaluate any value, and return True or False
print(bool("Hello")) # prints True, because the string is not empty

# numbers are True, except 0
# empty values are considered False
print(bool(0)) # prints False, because 0 is considered False

# Empty lists, tuples, sets, and dictionaries are also considered False
print(bool([])) # prints False, because the list is empty

# But list with values is considered True
print(bool([1, 2, 3])) # prints True, because the list is not empty

# print a message based on whether a condition is True or False
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# we can use the operator "and" to check if two conditions are True
# "and" returns True if both statements are true
# if one is false, it returns False
x = 5
print(x > 2 and x < 10) # prints True, because both conditions are True

# we can use the operator "or" to check if at least one condition is True
# "or" returns True if one of the statements is true
# if both are false, it returns False
x = 5
print(x > 2 or x < 4) # prints True, because one condition is True

# we can use the operator "not" to reverse the result, returns False if the result is true
x = 5
print(not(x > 2 and x < 10)) # prints False, because the result is True, and "not" reverses it to False

# we can combine "and", "or", and "not" in the same expression
x = 10
y = 20

resultado = (x > 5 and y < 25) or not(x == 10)
print(resultado) # prints True, because the first condition is True and the second is False, but "or" returns True if one condition is True

# functions can return a boolean value
def myFunction():
    return True
print(myFunction()) # prints True because the function returns "True"

# We can execute code based on the boolean value returned by a function
def mifuncion():
    return True
if mifuncion():
    print("Yes!") # prints Yes! because the function returns "True"
else:
    print("No!") # prints No! because the function returns "False"