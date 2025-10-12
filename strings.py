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