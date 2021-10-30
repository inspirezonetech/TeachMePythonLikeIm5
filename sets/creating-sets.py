# ------------------------------------------------------------------------------------
# Tutorial: Set Creation in Python
# A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.
# ------------------------------------------------------------------------------------

# A set is created by placing all the items (elements) inside curly braces {}, separated by comma, or by using the built-in set() function.
# It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello World", (1, 2, 3)}
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.
# my_set = {1, 2, [3, 4]} uncomment this line to see the error

# Distinguish set and dictionary while creating empty set
# initialize a with {}
a = {}

# check data type of a
print(type(a))

# initialize a with set()
a = set()

# check data type of a
print(type(a))

# we can make set from a list
my_set = set(["ice-cream", "burgar", "french-fries", "burgar"])
print(my_set)

# ------------------------------------------------------------------------------------
# Challenge: 
# 1. Create a set of numbers from 1 to 10 and print it.
# 2. Set cannot have duplicates - Create a set with duplicate values and print it. Observe the difference in output.
# ------------------------------------------------------------------------------------