# Lists, are used to store multiple items in a single variable.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Lists are created using square brackets []
# Lists are ordered, changeable, and allow duplicate values.

# Create a list
mylist = ["apple", "banana", "cherry"]
print(mylist) # prints the list

# Since lists are indexed, lists can have items with the same value 
mylist = ["apple", "banana", "cherry", "apple", "cherry"]
print(mylist) # prints the list with duplicate values

# To determine how many items a list has, use the len() function
print(len(mylist)) # prints 5, the number of items in the list

# To access an item in a list, use the index number
print(mylist[1]) # prints banana, the second item in the list (index starts at 0)

# List items can be of any data type
list1 = ["apple", "banana", "cherry"] # list of strings
list2 = [1, 5, 7, 9, 3] # list of integers
list3 = [True, False, False] # list of booleans

print(list1) # prints the list of strings
print(list2) # prints the list of integers
print(list3) # prints the list of booleans

# A list can contain different data types
list4 = ["abc", 34, True, 40, "male"]
print(list4) # prints the list with different data types

# We can create a list using the list() constructor
list5 = list(("pineapple", "orange", "grape")) # note the double round brackets
print(list5) # prints the list created with the list() constructor

# To access items in a list, use the index number inside square brackets []
print(list5[0]) # prints pineapple, the first item in the list

# We can also use negative indexing to access items from the end of the list
print(list5[-1]) # prints grape, the last item in the list

morefruits = ["mango", "kiwi", "watermelon", "pear", "peach", "plum", "pomegranate"]

# We can return a range of items by specifying where to start and where to end the range
print(morefruits[1:3]) # prints ['kiwi', 'watermelon'], from index 1 to 3 (3 not included)

# This example returns the items from the beginning to index 3 (not included)
print(morefruits[:3]) # prints ['mango', 'kiwi', 'watermelon']

# This example returns the items from index 4 to the end
print(morefruits[4:]) # prints ['peach', 'plum', 'pomegranate']

# range of negative indexes
print(morefruits[-4:-1]) # prints ['pear', 'peach', 'plum'], from the 4th last item to the last item (-1 not included)

# check if an item exists in a list, with the "in" keyword
if "kiwi" in morefruits:
    print("Yes, 'kiwi' is in the list of fruits") # prints Yes, 'kiwi' is in the list of fruits

# Change item values
# List: ["mango", "kiwi", "watermelon", "pear", "peach", "plum", "pomegranate"]
# change the second item (index 1) to "blackcurrant"
morefruits[1] = "blackcurrant" 
print(morefruits) # prints the list with the changed item (kiwi changed to blackcurrant)

# Change the items, using the range of index numbers
# List: ["mango", "kiwi", "watermelon", "pear", "peach", "plum", "pomegranate"]
morefruits[1:3] = ["blueberry", "raspberry"]
print(morefruits) # prints the list with the changed items (kiwi and watermelon changed to blueberry and raspberry)

# Change items, but with a range of item values, adding more items.
# List ["mango", "kiwi", "watermelon", "pear", "peach", "plum", "pomegranate"]
# change the second (index 1  to "blueberry") 
# a second element is added in index 2 to "raspberry"
morefruits[1:2] = ["blueberry", "raspberry"] 
print(morefruits) 
# the number of items in the list has increased
# List: ["mango", "blueberry", "raspberry", "watermelon", "pear", "peach", "plum", "pomegranate"]
# the list now has 8 items
# we replaced one item (kiwi) with two items (blueberry and raspberry)    

# to decrease the number of items in a list, we can use the range of index numbers to replace with fewer items
# List: ["mango", "blueberry", "raspberry", "watermelon", "pear", "peach", "plum", "pomegranate"]
morefruits[1:3] = ["kiwi"] 
print(morefruits)

# insert items
# we can use the insert() method to add an item at a specified index
morefruits.insert(2, "dragonfruit")
print(morefruits)