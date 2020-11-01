# ------------------------------------------------------------------------------------
# Tutorial: For-loops in Python
# ------------------------------------------------------------------------------------

# We use for loops when we have to access elements in a DS or while working within a range of numbers.
# One of the loops which helps us to iterate through a particular DS.

anime = ['Luffy', 'Naruto', 'Zoro', 'Midoriya', 'Lelouch', 'Levi', 'Natsu', 'Sanji', 'Shanks', 'Kakashi', 'Kageyama']

# What we have to do is print each of these names in list anime

for name in anime:
    print(name)

# This will help you to access and print each of the names in the list.

# Alternate

length = len(anime)

for i in range(length):
    print(anime[i])

# Also there is an |else| stance for each of the loops so here it is for for-loop:


for name in anime:
    print(name)
else:
    print('Loop has finished')

# It gives us a message when the loop is finished.

# Practice with the below challenge
# ------------------------------------------------------------------------------------
# Challenge: You have given a list of numbers and you have to output how many of the numbers are even and how many are odd.
#            list = [ 3, 21, 4, 56, 34, 69, 45, 63, 99 ]

#            Example : list = [ 2, 4, 5, 8, 34, 21 ]
#                      Output:- Odd : 2, Even : 4
#
# ------------------------------------------------------------------------------------
