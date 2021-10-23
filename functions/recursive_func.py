# ------------------------------------------------------------------------------------
# Tutorial: How to make a recursive function
#  A recursive function is a function that calls itself
# ------------------------------------------------------------------------------------
import sys
import StringIO

oldstdin = sys.stdin
sys.stdin = StringIO.StringIO('10')

# find the factorial of a user entered number
# the 'def' keyword is used to declare a function. the structure of a function is:
mul = 1
def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num - 1)

num = int(input('Enter a number to get the factorial of it: '))
if num == 0:
    print("Factorial of 0: 1")
else:
    print("Factorial of ", num, ":", fact(num))

# -----------------------------------------------------------------------------------
# Challenge: create a recursive function that makes a countdown from a user entered number till zero
# ------------------------------------------------------------------------------------
