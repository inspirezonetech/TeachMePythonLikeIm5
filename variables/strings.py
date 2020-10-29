# ------------------------------------------------------------------------------------
# Tutorial: brief description of tutorial content
# ------------------------------------------------------------------------------------

# In Python, strings are defined by enclosing charaters in either single quotation
# marks or double quotation marks

string1 = 'This is a string'
string2 = "This is also a string"

# Printing a string is the same as printing any variable
print(string1)              # This will print 'This is a string'

# Strings can be concatinated with a simple + sign
print(string1 + string2)    # This will print 'This is a stringThis is also a string'

# A string in Python is like an array of characters in C
print(string1[6])           # This will print 's'
print(string2[8:11])        # This will print 'als'

# If you wish to print a string with other variables amoung it, simply use a formatter
a = 5
b = 10
print('This is how we print the vaiable a = {} and b = {} with ease'.format(a, b))

# There are many tricks to you can do with strings and other operators when you get
# more comfortable with them!

# ------------------------------------------------------------------------------------
# Challenge: list challenges to be completed here. minimum of one challenge per tutorial
# ------------------------------------------------------------------------------------
# 1. Create a string & print out each character individually.
# 2. Create a string & find the length of it.
# 3. Print a string with different predefined variables in it.
# 4. Write a program that adds 'ing' to every string.
# 5. Write a program that replaces every 's' in a string with a '$'
