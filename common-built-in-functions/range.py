# ------------------------------------------------------------------------------------
# Tutorial: Range() built-in function in Python
# ------------------------------------------------------------------------------------

# Code here explaining concept with comments to guide


# Range func is inbuilt function having arguments passed to it below:
# if we use just a single argument range(n) - it takes 0 by default as starting point and follows for n values i.e. ending at n-1
# range(n) = range(0,n) as exclusive of its upper limit.
# range(start,stop,step) {start is inclusive and stop is exclusive and step is the value of increament or decreament in each iteration of numbers
# { By default, if we do not state the third argument it is taken as +1 }

# Syntax:

n = 5

x = range(0, n, 1)  # goes from 0 to n-1 with step size of 1 equal to range(n)

y = range(n, 0, -2)  # goes from n to 1 with step size of -2

# So range deals with both increament as well as decreament hence very useful while calling for loops.
# Also range() returns a sequence of numbers included in | range(start,stop,step) |

# ------------------------------------------------------------------------------------
# Challenge: Take user based input n and then compute the sum of first n natural numbers and print the sum.
# ------------------------------------------------------------------------------------
