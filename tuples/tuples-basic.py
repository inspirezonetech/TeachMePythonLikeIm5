# ------------------------------------------------------------------------------------
# Tutorial: Tuple basics
# ------------------------------------------------------------------------------------
# A tuple is just like a list. But one difference is that items are enclosed with
# (parentheses), instead of [brackets].
my_tuple = ("Tuple", "is", "fun")

# It can also store variables of different types:
my_tuple2 = (123, 1.0, "Hello", "World!", True)

# Another notable difference is that tuple items are immutable.
# Immutable means the items cannot be updated or changed.
# Although you can still index an item like this:
last_item = my_tuple2[-1]

# This won't work (Commented out, otherwise it'll cause an error):
# my_tuple2 = False

# To initialize an empty tuple, you can just write empty parentheses.
empty_tuple = ()
# But interestingly, to define a tuple that consists of one item,
# you don't write parentheses. Instead, you just add a trailing comma.
tuple_with_one_item = "one",

# Just like a list, you can count how many items a tuple has by using len():
print(len(my_tuple))
# Output: 3

# When you unpack multiple items to one variable, Python actually creates a tuple
# behind-the-scenes.
t = 101010, True, "Neon"
print(t)
# Output: (101010, True, 'Neon')
# You can also do the reverse operation:
x, y, z = t
print(x, y, z)
# Output: 101010 True Neon

# ------------------------------------------------------------------------------------
# Challenge: Create a tuple that stores each word in your name as strings.
# Then, unpack the tuple into multiple variables. You can call the variables whatever
# you want. (One example: first_name, middle_name, last_name)
# ------------------------------------------------------------------------------------
# Create your tuple here.

# Unpack the tuple here.
