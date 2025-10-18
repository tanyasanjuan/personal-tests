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