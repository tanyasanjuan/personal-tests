saludo = "Hello, World!"
print(saludo)
# strings are arrays of bytes representing unicode characters
# we can access the characters of a string using indexing 
print(saludo[0]) # prints H, the first character of the string
print(saludo[1]) # prints e, the second character of the string

# we can return a range of characters by specifying where to start and where to end the range
print(saludo[1:3]) # prints "el", from position 1 to 3 (3 not included)
print(saludo[3:5]) # prints "lo", (a space is a character too), from position 3 to 5 (5 not included)
print(saludo[:5]) # prints "Hello", from the beginning to position 5 (not included)
print(saludo[3:]) # prints "lo, World!", from position 3 to the end
#negative indexing means start from the end
print(saludo[-1]) # prints "!", the last character of the string
print(saludo[-5:-2]) # prints "orl", from the "o" in "World!" 5th position, not included the last 2 positions (d and !)

# since string are arrays we can loop through them, with a "for" loop
for fruta in "banana":
    print(fruta) # prints each character of the string "banana"

# to get the length of a string we can use the len() function
print(len(saludo)) # prints 10, the length of the string "Hi, World!"

# Check if a certain phrase or character is present in a string, with the "in" keyword
txt = "The best things in life are free!"
print("free" in txt) # prints True

# if statement
if "free" in txt:
    print("Yes, 'free' is present.") # prints Yes, 'free' is present.

# Check if a certain phrase or character is NOT present in a string, with the "not in" keyword
print("expensive" not in txt) # prints True, because "expensive" is NOT present in txt

# check if "expensive" is NOT present in txt, with an if statement
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.") # prints No, 'expensive' is NOT present.

# Uppercase and Lowercase
mayusculas = "soy grande"
print(mayusculas.upper()) # prints the string in uppercase
print(mayusculas.lower()) # prints the string in lowercase

# Remove whitespace from the beginning or the end of a string
whitespace = "   Hola Mundo   "
print(whitespace.strip()) # prints "Hola Mundo", without the whitespace

# Replace a string with another string
reemplazo = "Hola Mundo"
print(reemplazo.replace("Mundo", "Universo")) # prints "Hola Universo"

# Split a string into a list where each word is a list item
division = "Hola Mundo, bienvenidos a Python"
print(division.split()) # prints ['Hola', 'Mundo,', 'bienvenidos', 'a', 'Python']

# we can't combine strings and numbers, for example:
# age = 36
# txt = "My name is John, I am " + age
# print(txt) # this will raise an error because age is an integer and cannot be concatenated to a string
# but we can convert the number into a string before concatenation

# concatenate strings and numbers with the str() function
age = 36
txt = "My name is John, I am " + str(age)
print(txt) # prints My name is John, I am 36

# we can also use the format() method to concatenate strings and numbers
age = 36
txt = "My name is John, I am {}".format(age)
print(txt) # prints My name is John, I am 36

# we can write it in a simpler way with f-strings (available in Python 3.6 and later)
# To specify a string as an f-string, put an f in front of the string, 
# and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt) # prints My name is John, I am 36

# a placeholder to display the result of an expression inside a string
price = 5
txt = f"The price is {price} dollars"
print(txt) # prints The price is 5 dollars

# the placeholder can include a modifier to format the result
price = 49
txt = f"The price is {price:.2f} dollars" # .2f means 2 decimal places
print(txt) # prints The price is 49.00 dollars

# a placeholder to display the result of a mathematical operation inside a string
price = 49
txt = f"The price is {price + 1} dollars"
print(txt) # prints The price is 50 dollars

# scape characters
# to include special characters in a string, we can use the backslash \ as an escape character
# for example, to include a double quote in a string that is enclosed in double quotes,
escapes = "We are the so-called \"Vikings\" from the north."
print(escapes) # prints We are the so-called "Vikings" from the north.

# other escape characters are:
# \' 	Single Quote
txt = "It\'s alright."
print(txt) # prints It's alright.

# \\ 	Backslash
txt = "This is a backslash: \\"
print(txt) # prints This is a backslash: \

# \n 	New Line
txt = "Hello\nWorld!"
print(txt)
# \r 	Carriage Return
txt = "Hola\rborola!"
print(txt)
# \t 	Tab
# \b 	Backspace
# \f 	Form Feed
# \ooo 	Octal value
# \xhh 	Hex value

# string methods
# there are many string methods available in Python, here are some examples:    
print(saludo.capitalize()) # Capitalizes the first letter of the string
print(saludo.count("o")) # Counts the number of occurrences of a substring in the string (letter o appears 2 times in "Hello, World!")

# Finds the first occurrence of a substring in the string 
# (returns the index of the first character of the substring, 
# in this case it returns 7, because "World" starts at index 7 in "Hello, World!")
print(saludo.find("World")) 

# Here it returns 1, because "e" is the second character in "Hello, World!" (index starts at 0)
print(saludo.find("e"))

# Finds the first occurrence of "l" between index 1 and 10, returns 2
# 2 is the index of the first "l" in "Hello, World!" after index 1
print(saludo.find("l", 1, 10)) # Finds the first occurrence of "l" between index 1 and 10, returns 2

# if the substring is not found, it returns -1
print(saludo.find("k")) # returns -1 because "k" is not found

print(saludo.isalpha()) # Checks if all characters in the string are alphabetic
print(saludo.isdigit()) # Checks if all characters in the string are digits
