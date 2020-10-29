# ------------------------------------------------------------------------------------
# Tutorial: indexing lists
# ------------------------------------------------------------------------------------
# Here you go ! You have lists in python, it's like a fridge,
# and you can store things to a specific place and get them when you want,
# if you remember correctly where you put things !


# a list is with brackets and you can add what you want by separating it with commas
# here, you have a list with fruits (type String)
my_list = ["banana", "apple", "strawberry", "grape", "pear"]

# but you can store things which aren't all the same type
my_crazy_list = [1, 3, "red", "blue", True]


# To access to something of your list we use the index. It's start from 0 to the
# length of you list minus 1 (because it's start from 0)

# to know the index of something of an element in your list we use the method index()
index = my_list.index('apple')
print('The index of apple:', index)
# output: 1


# you can also search the index of an element in part of the list,
# you need to give the start and the end
index = my_list.index('grape', 1, 4)
print('The index of grape:', index)
# output: 3


# If you want to see what is on a specific index you just need to call the variable
# where you have stored your list with bracket and the specific index
magic_fruit = my_list[2]
print('Your magic fruit is:', magic_fruit)

# ------------------------------------------------------------------------------------
# Challenge: get the right answer !
# ------------------------------------------------------------------------------------
# Use what you have seen just before to resolve the challenge

colors = ["blue", "red", "purple", "orange", "white", "grey", "yellow", "black", "green"]

# Change the value None to the index of the color grey
index_grey = None
print('You must see here the index of the color grey:', index_grey)

# Change the value None to access to the color purple with the right index
purple = None
print('You must see here the color purple:', purple)

# uncomment lines bellow to see if your results is correct
# Will throw an error if your solution is incorrect

# assert(index_grey == 5)
# assert(purple == 'purple')
