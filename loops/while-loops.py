# ------------------------------------------------------------------------------------
# Tutorial: brief description of tutorial content
# ------------------------------------------------------------------------------------
# Here we will look into how to use one of the loops - while loop to generate desired outputs with certain condition
# Syntax: After while we pass the condition to be checked

t = 0
while t < 10:
    t = t + 2
    print(t)

# Also we can use an |else| stance with the while loop as if the condition don't satisfy and we need a last statement to be executed after the while loop is finished:

t = 0
while t < 10:
    t = t + 2
    print(t)
else:
    print("loop finished")

# So above loop will work till the specified condition is satisfied hence will run about 5 times in this case


# Reverse the Number:
# What we need to do is take n as input and print the reversed n.
# 
# 
# 
# ------------------------------------------------------------------------------------
# Challenge: Take a user input n and find and print the reverse of the number. Also you don't have to print trailing zeroes while reversing.
#            Example: 1.) Input - 2345 , Output - 5432
#                     2.) Input - 2480 , Output - 842
# ------------------------------------------------------------------------------------
