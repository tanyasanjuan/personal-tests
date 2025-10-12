# Rules for write in python

# Comments start with a #, and Python will ignore them
# strings can be defined with single or double quotes, both are correct
# a = "Hi"
# b = 'Hi'

print ("Hello, World!")  

# assigning a string to a variable and printing it
a = "Hi, World!"
print(a)

# strings are arrays of bytes representing unicode characters
# we can access the characters of a string using indexing 
print(a[0]) # prints H, the first character of the string
print(a[1]) # prints i, the second character of the string

# since string are arrays we can loop through them, with a "for" loop
for x in "banana":
    print(x) # prints each character of the string "banana"

# to get the length of a string we can use the len() function
print(len(a)) # prints 10, the length of the string "Hi, World!"

# Indentation is very important in python
    # Indentation is used to define a block of code
    # Use 4 spaces per indentation level

if 5 > 2:
    print("Five is greater than two!")  # Indented block

# Variables
# Variables, asign values to them, like containers of values 
# can be created using the assignment operator (=)
# Variable names can contain letters, numbers, and underscores
# names cannot start with a number 
x = 5
y = "Hola mundo" 

print(x)
print(y)

# Can be Variable changed after they have been set, from string to int, for example
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x) # prints "Sally" because x was changed, so it prints the new value

# Casting
# If you want to specify the data type of a variable, this can be done with casting
x = str(5)    # x is now of type str
y = int("10") # y is now of type int
z = float(10) # z is now of type float

print(x)
print(y)
print(z)
print(type(x)) # prints the type of x, to check the type of a variable "class 'int'"
print(type(y)) # prints the type of y   
print(type(z)) # prints the type of z

# Variables are case-sensitive, uppercase and lowercase letters are different
# age = 4
# Age = "Sally"
# AGE = "John"
a = 4
A = "Sally" 
print(a) # prints 4
print(A) # prints "Sally"

# Variable names, can be of any length, can contain letters, numbers, and underscores
# but cannot start with a number "age2 - is correct" "2age - is not correct" 
# It's better if the names are descriptive
# instead of using x, y, z use more descriptive names like: my_nationality, my_name, my_age
# underscores are fine "my_name - is correct" "my-name - is not correct"
# Variable names cannot contain spaces " my name - is not correct" "my_name - is correct"

# Variables can't be python keywords: 
# if, else, while, for, break, continue, return, in, is, not, and, or, def, class, try, 
# except, finally, with, as, lambda, pass, yield, import, from, global, nonlocal, assert, del, raise

# Multiword variable names
# There are several techniques for naming multiword variables:
# 1. Camel Case: myVariableName
# 2. Pascal Case: MyVariableName
# 3. Snake Case: my_variable_name

# We can assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x) # prints "Orange"
print(y) # prints "Banana"  
print(z) # prints "Cherry"

# The number of variables must match the number of values
# x, y, z = "Orange", "Banana" # This will raise an error
# x, y, z = "Orange", "Banana", "Cherry", "Apple" # This will raise an error

# Assign the same value to multiple variables, we can do it like this:
x = y = z = "Orange"
print(x) # prints "Orange"
print(y) # prints "Orange"
print(z) # prints "Orange"

# Unpack a collection, we can extract the values into variables like this:
fruits = ["Manzana", "Platano", "Cereza"]
x, y, z = fruits
print(x) # prints "Manzana"
print(y) # prints "Platano"
print(z) # prints "Cereza"

# Output variables
# The Python print() function is used to output variables (to show the value on the screen)
x = "Python is awesome"
print(x) # prints "Python is awesome"

# To display multiple variables, we can use the comma operator
# The , operator is used to separate variables when printing
x = "Python"
y = "is"
z = "fun"
print(x, y, z) # prints "Python is fun"


# To display multiple variables, we can use the "+" operator
x = "Python"
y = "is"
z = "great"
print (x + y + z) # prints "Pythonisgreat" # No spaces between words
# To add spaces between words, we can add a space in the strings
# x = "Python "
# y = "is "
# z = "great"
# other solution is to add spaces in the print function as follows:
print(x + " " + y + " " + z) # prints "Python is awesome is great"

# The + operator is used to concatenate strings
# The + operator can also be used to add numbers (in this case, it performs addition)
x = 5
y = 10
print(x + y) # prints 15

# The + operator cannot be used to concatenate strings and numbers
# Combine a string and a number, with the + operator will raise an error
# x = 5
# y = "John"
# print(x + y) # This will raise an error
# error: TypeError: unsupported operand type(s) for +: 'int' and 'str'
# we can use a comma instead of + to separate them
x = 5
y = "John"
print(x, y) # This will print "5 John"

# To combine a string and a number, we can use the str() function to convert the number to a string
# x = 5
# y = "John"
# print(x + str(y)) # This will print "5 John"

# Global Variables
# Variables that are created outside of a function 
# (as in all of the examples above) are known as global variables
# Global variables can be used by everyone, both inside of functions and outside
# and it can be used anywhere in the code.

x = "increible" # global variable
def myfunc():
    print("Python es " + x) # using the global variable inside the function
myfunc() # prints "Python es increible"

# If you create a variable with the same name inside a function,
# this variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value

x = "increible" # global variable
def myfunc():
    x = "fantastico" # local variable
    print("Python es " + x) # using the local variable inside the function
myfunc() # prints "Python es fantastico"

print("Python es " + x) # prints "Python es increible" because the global variable is unchanged

# To create a global variable inside a function, we can use the global keyword
def myfunc():
    global x # declare x as a global variable
    x = "maravilloso" # create a global variable
myfunc() # call the function to create the global variable
print("Python es " + x) # prints "Python es maravilloso" because x is now a global variable

# To change the value of a global variable inside a function, we can use the global keyword
x = "increible" # global variable
def myfunc():
    global x # declare x as a global variable
    x = "fantastico" # change the global variable
myfunc() # call the function to change the global variable
print("Python es " + x) # prints "Python es fantastico" because x is now changed