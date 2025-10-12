# using operators
print (2 + 3) # addition
print (5 - 2) # subtraction
print (3 * 4) # multiplication
print (10 / 3) # division
print (10 // 3) # division without decimal part
print (1 + 2 * 3) # operator precedence (it says that multiplication is done before addition, that's why the result is 7 and not 9)
# parentheses can be used to change the precedence
print ((1 + 2) * 3) # now the result is 9 because the addition is done first
# in maths the order of precedence is: multiplication and division, addition and subtraction (PEMDAS)
print (1 + (2 *3)) # result is 7
print (10 % 2) # modulus, gives the remainder of the division, in this case the result is 0 because 10 is divisible by 2
print (10 % 3) # modulus, gives the remainder of the division, in this case the result is 1 because 10 is not divisible by 3

# a number equal to another number is assigned with the = operator
x = 5
y = 10
z = 5
print(x == z) # prints True because x is equal to z
print(x == y) # prints False because x is not equal to y

# range
x = range(5) # range from 0 to 4
print(x) # prints range(0, 5)
print(list(x)) # convert to list to display the content of x, so it prints [0, 1, 2, 3, 4]

y = range(1, 6) # range from 1 to 5
print(list(y)) # prints [1, 2, 3, 4, 5]

z = range(1, 10, 2) # range from 1 to 9 with a step of 2 (odd numbers)
print(list(z)) # prints [1, 3, 5, 7, 9]

# Convert Types
# we can't convert complex number into another number type
# we can't convert from string to int or float if the string contains a number
# but if the string contains letters, it will give an error
# for example: "5" is a string and cannot be converted to int or float
# but "five" cannot be converted to int or float because it contains letters
# x = "5" # string
# y = int(x) # this will raise an error because x is a string that contains a number
# print(y) # error: ValueError: invalid literal for int() with base 10

# we can convert between different types, for example, from int to float and from float to int.
x = 5 # integer
y = 2.5 # float

x = float(x) # convert int to float
print(x) # prints 5.0

# when converting from float to int, the decimal part is removed (not rounded)
y = int(y) # convert float to int (removes the decimal part)
print(y) # prints 2

# random number
# Python doesn't have random() function to generate a random number
# but we can use the random module to generate random numbers
import random
print(random.randrange(1, 10)) # prints a random number between 1 and 9 (10 is excluded)