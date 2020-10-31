# ------------------------------------------------------------------------------------
# Tutorial: Using continue keyword in python
# ------------------------------------------------------------------------------------

# It allows us to leave some piece of code when we do not need it or some fixed condition is not met.
# It is just a keyword which allows us to handle our code in specific conditions.
# for example if we say that a particular var has achieved a particular val then we don't proceed with the piece of code after the continue keyword.

# Note : We also use it when we have some base cases for our test cases while doing competitive programming.

# Note: continue keyword is only used within loops.

# Example:

for x in range(5):
    if x == 3:
        continue
    print(x)

# In above example as x approaches the value 3 (as in condition) continue statement is trigerred an thus when we look at the output of the code, x=3 is not printed.
# Also there are times we don't want to do anything in a particular condition so what we do is just use the continue statement to keep the iteration going on.

for x in range(1, 16):
    if x % 5 == 0:
        continue
    print(x)

# Above example states that when there will be a number in the range which is a multiple of 5 so it will not execute print statement
# Hence, our output will contain all elements in the range which are not multiple of 5.

# Basically, the code above the continue keyword is considered only if the above condition does not satisfy else the code will process the request and exclude the lines of code below continue.

# ------------------------------------------------------------------------------------
# Challenge: Take user input n and print all the odd natural numbers  ( where natural numbers is the list - [1,2,3,4,5...,n] ) upto n using continue keyword.
#            Example: Input - 18
#                     Output - { 1, 3, 5, 7, 9, 11, 13, 15, 17 } [ Just consider the values not the pattern ]
# ------------------------------------------------------------------------------------
