# ------------------------------------------------------------------------------------
# Tutorial: Learn how to alter lists.
# ------------------------------------------------------------------------------------

my_list = [10, 11, 12]
print("Original list")
print(str(my_list) + "\n")

# To add an item to the end of a list use append()
my_list.append(15)  # Will add the integer 15 to the end of the list.
print("List after appending ")
print(str(my_list))

# To add an item at a specific index use inset()
my_list.insert(1, 6)  # Adds an item at second position
print("List after inserting ")
print(str(my_list))

# To append another list to your list use extend()
new_list = [7, 8, 9]
my_list.extend(new_list)
print("List after extending ")
print(str(my_list))
print("")

# To remove an item from the list use remove()
# Will throw an error if the item doesn't exist in the list
# If an item is present in the list more than once only the first
# copy will be removed from the list
my_list.remove(6)
print(str(my_list))

# To remove an item from the list and return it for further use use pop()
popped = my_list.pop(5)  # Will remove the number 8 and return it
print("Popped item " + str(popped))
print(str(my_list))
print("")

# To sort a list without altering the original data use sorted()
sorted_list = sorted(my_list)
print("Original list")
print(str(my_list))
print("Sorted copy")
print(str(sorted_list))
print("")

# To sort a list use sort()
# Sort takes an optional function
my_list.sort()
print("Sorted list " + str(my_list))
print("")

# To empty a list use clear()
my_list.clear()
print("Emptied list " + str(my_list))

# ------------------------------------------------------------------------------------
# Challenge: You are in charge of sorting test scores for an exam.
# There are some results missing as in the following points:
# Add the integer 1 to any position in the list
# Add the integer 50 to the end of the list
# Add the list 45, 33, 16 to the end of the list
# then sort the list so it is ordered largest number to smallest
# (eg 100, 50, 45, 33, 25, 22, 16, 10, 5, 3, 1)
# Print the first score in the list to declare the winner of the exam.
# ------------------------------------------------------------------------------------

print("\n\nChallenge 1:")
list_to_sort = [100, 5, 10, 25, 3, 22]
# Perform operations here

print(str(list_to_sort))
# Fix and uncomment print line below to declare the winner
# print("The winner is" + )

# Uncomment the assert line below once you have performed the required actions
# Will throw an error if your solution is incorrect
# assert(list_to_sort == [100, 50, 45, 33, 25, 22, 16, 10, 5, 3, 1])
