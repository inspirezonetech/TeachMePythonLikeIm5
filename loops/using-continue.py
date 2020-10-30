# ------------------------------------------------------------------------------------
# Tutorial: Using continue keyword in python
# ------------------------------------------------------------------------------------

# It allows us to leave some piece of code when we do not need it or some fixed condition is not met.
# It is just a keyword which allows us to handle our code in specific conditions.
# for example if we say that a particular var has achieved a particular val then we don't proceed with the piece of code after the continue keyword.
# Note : We also use it when we have some base cases for our test cases while doing competitive programming.
# Also note that continue keyword is only used in the case of loops.


for x in range(5): 
    if x == 3:
        continue
    print(x)
    

# In above example as x approaches the value 3 (as in condition) continue statement is trigerred an thus when we look at the output of the code, x=3 is not printed.
# We can conclude that after the condition achieved our code was not given permission to increase the val of t.
# Also there are times we don't want to do anything in a particular condition so what we do is just use the continue statement to keep the iteration going on.

# Basically, the code below the continue keyword is considered only if the above condition does not satisfy else the code will process the request and exclude the lines of code below continue. 

# ------------------------------------------------------------------------------------
# Challenge: Take user input n and print all the odd natural numbers upto n using continue keyword.
# ------------------------------------------------------------------------------------
