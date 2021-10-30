# ------------------------------------------------------------------------------------
# Tutorial: Removing Elements in a Set
# A particular item can be removed from a set using the methods discard() and remove().
# ------------------------------------------------------------------------------------

# The only difference between the two is that the discard() function leaves a set unchanged if the element is not present in the set. On the other hand, the remove() function will raise an error in such a condition (if element is not present in the set).

# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# ------------------------------------------------------------------------------------
# Challenge: Remove an element which is not present in my_set and print the set. Observe the output. Check which type of error it is and why it occurs.
# ------------------------------------------------------------------------------------