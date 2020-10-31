# ------------------------------------------------------------------------------------
# LIST
# List is a collection which is ordered and changeable.
# ------------------------------------------------------------------------------------
# Code here explaining concept with comments to guide
# Syntax:
# empty list
lst = []
# list of integer
lst = [1, 2, 3, 4, 5]
# list with various data type
lst = [1, "hello", 3.55]
# nested list
lst = [1, [8, 3, 4, 5], "hello"]
# retrieval of elements using list index
print(lst[0])  # this will print first element of the list that is [1]
# negative index
print(lst[-1])  # output: ["hello"]
# there are some in-built function available in the python for the list, like
# lst.sort()  # this will arrange the element in the ascending order.
lst.append(9)  # this will add element in the end of the list.
lst.remove(9)  # this will remove the element 9 from the list.
lst.insert(1, 9)   # this will add insert the element 9 at index place 1.
del lst[0:2]  # this will delete the element in the range 0-2.
lst.count(9)   # this will return the no of argument passes.
# ------------------------------------------------------------------------------------
# Challenge: list challenges to be completed here. minimum of one challenge per tutorial
# 1. take input from the user into the list
# ------------------------------------------------------------------------------------
