# ------------------------------------------------------------------------------------
# Tutorial: brief description of tutorial content
# ------------------------------------------------------------------------------------

# Code here explaining concept with comments to guide


# Range func is inbuilt function having arguments passed to it below:
# if we use just a single argument range(n) - it takes 0 by default as starting point and follows for n values i.e. ending at n-1
# range(n) = range(0,n) as upper limit is not included , max to max (upper limit - 1) is included in range
# range(l,u,inc) {l = lowerlimit, u = upperlimit, inc = increament like what we need to be the gap between each iteration of numbers
# by default if we do not use the third argument it is taken as +1 . inc can be negative as well}

# Syntax:

n = 5

x = range(0, n, 1)  # goes from 0 to n-1 with inc of 1 equal to range(n)

y = range(n, 0, -2)  # goes from n to 1 with inc of -2

# So range deals with both increament as well as decreament hence very useful while calling for loops


# Lets give a challenge to try out what we learnt:
# Like what we need to do is compute sum of first n natural numbers by using the range function and not the formula.

# ------------------------------------------------------------------------------------
# Challenge: list challenges to be completed here. minimum of one challenge per tutorial
# ------------------------------------------------------------------------------------