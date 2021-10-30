# ------------------------------------------------------------------------------------
# Tutorial: Set Modification in Python
# Sets are mutable. However, since they are unordered, indexing has no meaning.
# We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.
# ------------------------------------------------------------------------------------

# We can add a single element using the add() method, and multiple elements using the update() method. The update() method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.

# initialize a
a = {1, 3}
print(a)

# a[0]
# if you uncomment the above line
# you will get an error
# TypeError: 'set' object does not support indexing

# add an element
# Output: {1, 2, 3}
a.add(2)
print(a)

# add multiple elements
# Output: {1, 2, 3, 4}
a.update([2, 3, 4])
print(a)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
a.update([4, 5], {2, 6, 8})
print(a)

# ------------------------------------------------------------------------------------
# Challenge: Create a new set b and Update the set a to include the elements of set b.
# ------------------------------------------------------------------------------------