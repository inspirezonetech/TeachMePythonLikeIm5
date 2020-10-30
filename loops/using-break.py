# ------------------------------------------------------------------------------------
# Tutorial: How to use break statements within loops.
# ------------------------------------------------------------------------------------

# Break statements are useful to use with loops in Python. They allow for a loop to be
# 'broken out of' or 'escaped'. Break is mainly used when a condition is met, and we
# want to immediately exit a loop

for letter in 'Python':
    print(letter)
    if letter == 't':
        break     # if the letter 't' was found, then the break will stop the for loop

# If nested loops are being used, the break statement will exit the innermost
# enclosing loop.

for y in range(2, 10):
    for x in range(2, y):
        if y % x == 0:
            print('{} equals {} * {}'.format(y, x, y / x))
            break     # the if statement is exited, but the for loops are still active
        else:
            print(y, 'is a prime number')

# ------------------------------------------------------------------------------------
# Challenge: list challenges to be completed here. minimum of one challenge per tutorial
# ------------------------------------------------------------------------------------
# 1. Search for a letter in a string & break out of loop when it has been found.
# 2. Create a while loop that
# (a) opens a file
# (b) writes a number to the file
# (c) closes the file.
# When the file has 100 lines, break out of the loop and print the content of the file.
