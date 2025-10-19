 # we can loop through a list even if we modify it during the loop
my_list = ["banana", "manzana", "fresa"]
for fruit in my_list:
    print(fruit)

# We can also loop through a list using index values
my_list = ["banana", "manzana", "fresa"]
for i in range(len(my_list)):
    print(my_list[i])

# We can loop through a list in reverse order
my_list = ["banana", "manzana", "fresa"]
for fruit in reversed(my_list):
    print(fruit)

# We can loop through the list by referring to their index numbers
my_list = ["banana", "manzana", "fresa"]
for i in range(len(my_list)):
    print(my_list[i])
# however it's easier to use the for loop directly on the list, as the 1st example shows.
#for fruit in my_list:
#   print(fruit)

# We can also use a while loop to loop through a list
my_list = ["banana", "manzana", "fresa"]
i = 0
while i < len(my_list):
    print(my_list[i])
    i = i + 1
# however it's easier to use the for loop directly on the list, as the 1st example shows.

# Looping using list comprehension
# List comprehension offers a shorter syntax 
# when you want to create a new list based on the values of an existing list.
my_list = ["banana", "manzana", "fresa"]
[print(fruit) for fruit in my_list]
# however it's easier to use the for loop directly on the list, as the 1st example shows.
# Note: List comprehensions are generally used to create new lists,
# so using them just for printing is not a common practice.
# But it's included here to demonstrate the concept.

# We can use the comprehension to loop when:
# - We want to create a new list based on the existing list
# - We want to apply a transformation to each element
my_list = ["banana", "manzana", "fresa"]
uppercased_fruits = [fruit.upper() for fruit in my_list]
print(uppercased_fruits)  # Output: ['BANANA', 'MANZANA', 'FRESA']

# - We want to filter elements based on a condition
# the syntax is: [expression for item in iterable if condition == True]
# the return value is a new list, leaving the original list unchanged
# condition is like a filter that only accepts items that evaluate to True (listed items)
# The condition if x != "banana" will return True for all elements other than "banana"
# making the new list contain all fruits except "banana".
# the condition is optional, and can be omitted.
my_list = ["banana", "manzana", "fresa", "kiwi", "mango"]
filtered_fruits = [fruit for fruit in my_list if "a" in fruit]
print(filtered_fruits)  # Output: ['banana', 'manzana', 'fresa', 'mango']

# to generate even numbers from 0 to 10
even_numbers = [num for num in range(11) if num % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10]

# The iterable can be any iterable object, like a list, tuple, set, etc.
# We can use range() to generate a sequence of numbers
nuevalista = [x for x in range(10)]
print(nuevalista)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# we can add a condition to filter the numbers
nuevalista = [x for x in range(10) if x < 5]
print(nuevalista)  # Output: [0, 1, 2, 3, 4]