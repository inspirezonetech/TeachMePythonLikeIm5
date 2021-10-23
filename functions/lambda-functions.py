# ------------------------------------------------------------------------------------
# Tutorial: Lambda Function in Python
# ------------------------------------------------------------------------------------

# Lambda functions are the anonymous functions which do not need
# to be defined with names but the keyword 'lambda'. A lambda
# function takes any number of arguments and evaluates the expression of it.


# Syntax => (lambda arguments: expression)(arguments)
print((lambda y: y * 10)(3))


# ------------------------------------------------------------------------------------
# A lambda function can also be assigned to a variable and then called as an object.
# Example:
# x = lambda y: y * 10
# print(x(3))
# ------------------------------------------------------------------------------------


# Usage with multiple arguments
sumup = (lambda a, b: a + b)(3, 5)
print(sumup)

# Usage with print
(lambda x: print(x))("Great Work!")

# Usage with If-Else
minimum = (lambda a, b: a if(a < b) else b)(10, 100)
print(minimum)


# ------------------------------------------------------------------------------------
# Challenge: Create a lambda function which can take 3 arguments and evaluates the
# product of it. Print the result in the console by passing the parameters.
# Example => Inputs: 2,3,4 || Output: 24
# ------------------------------------------------------------------------------------


# Pre-requisites : Functions in Python
# Unlike defined functions, a Lambda function cannot have more
# than one expression and do not need return statement.
# Use Lambda when a function is needed for short period of time.

# Usage of Lambda within Defined functions
def sample(n):
    m = (lambda a: abs(a) + 1)(n)
    return 1000 * m

print(sample(-3))

# ------------------------------------------------------------------------------------
# Challenge: Create a lambda function within the max_cube() function to find the
# maximum of two given arguments, and then return the cube of the same.
# ------------------------------------------------------------------------------------

def max_cube(a, b):
    pass

print(max_cube(2, 3))  # Once you have completed the challenge, it should print : 27
