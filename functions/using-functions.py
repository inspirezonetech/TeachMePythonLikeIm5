# ------------------------------------------------------------------------------------
# Tutorial: how to declare and call a function
# ------------------------------------------------------------------------------------

# the 'def' keyword is used to declare a function. the structure of a function is:
def a_function():
    print('hello world')

# to call a function simply type its name
a_function()

# you can declare functions that accept arguments
def another_function(argument1, argument2):
    print(argument1, argument2)

# when calling a function with arguments, pass in the arguments
another_function('hello', 'universe')


# -----------------------------------------------------------------------------------
# Challenge: create a function that takes two integers as arguments and prints the sum.
# call the function and pass the values '1' and '2' to the function
# ------------------------------------------------------------------------------------
