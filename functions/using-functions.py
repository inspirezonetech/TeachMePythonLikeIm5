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








# ---------------------------------------------------
# More on functions
# ---------------------------------------------------

# Functions can return something with the 'return' keyword.
def biggestNumber(number1, number2):
    maxnumber = max(number1, number2) # The max keyword returns the highest value of all those passed

    return maxnumber

# When calling the function, you can use the value returned
oldestPerson = biggestNumber(15, 18)
print("Oldest person:", oldestPerson)

print( biggestNumber(100*0, 1*2) )

# -----------------------------------------------------------------------------------
# Challenge: modify the previous function you create so it returns the value instead.
# create another piece of code that uses the value returned from that function
# ------------------------------------------------------------------------------------

