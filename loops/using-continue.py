# ------------------------------------------------------------------------------------
# Tutorial: brief description of tutorial content
# ------------------------------------------------------------------------------------

# It allows us to leave some piece of code when we do not need it or some fixed condition is not met
# It is just a keyword which allows us to handle our code in specific conditions 
# for example if we say that a particular var has achieved a particular val then we don't proceed with the piece of code after the continue keyword


# Code here explaining concept with comments to guide
t = 0

for x in range(5):
    print(t)
    if t == 3:
        continue;
    t = t + 1

# In above example after t approaches val 3 t stops increamenting so hence aur output will be like 0 1 2 3 3 (just concentrate on values not the pattern)
# We can conclude that after the condition achieved our code for not given permission to increament the val of t.
# Also there are times we don't want to do anything in a particular condition so what we do is just use the continue statement to keep the iteration going on.


# Note : We also use it when we have some base cases for our test cases while doing competitive programming 

# As we understood enough of the theory part now we require to implement it and watch how it goes
# Challenge:
# So what we need to do is print only odd numbers upto n where n is user based input using continue statement





# ------------------------------------------------------------------------------------
# Challenge: list challenges to be completed here. minimum of one challenge per tutorial
# ------------------------------------------------------------------------------------
