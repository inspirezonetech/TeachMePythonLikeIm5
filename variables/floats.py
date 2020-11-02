# -----------------------------------------------------
# Tutorial: An explanation of the float datatype
# -----------------------------------------------------

# In python, decimals are stored using the float datatype
number1 = 10.10  # We can directly assign a decimal to a variable
# We can check the datatype of a variable using the type function. So let's verify if the variable number1 is a float or not
print("Type of number1 is", type(number1))
# We can see that Python is smart enough to make the variable as a float. This is called Dynamically typed.

# We can also declare a decimal using the float() function
number2 = float(20.20)
# We can see that the variable number2 is a float too. This is called Static typed as we are giving the type before itself
print("Type of number2 is", type(number2))

# We can also convert from other datatype to decimal using the float()
number3 = float("30.30")
# Python converts the string to a float.
print("Type of number3 is", type(number3))
number3 = float(30)
# Python converts the int to a float.
print("Type of number3 is", type(number3))

# Floats can be negative decimals too
number4 = -10.10
print("Type of number4 is", type(number4))


# Operations on float

# Addition: Two floats can be added using the + sign
sum = number1 + number2
print(f'{number1} + {number2} is {sum}')

# Subtraction: Floats can be subtracted using the - sign
diff = number3 - number2
print(f'{number3} - {number2} is {diff}')

# Multiplication: Two floats can be multiplied using the * sign
mul = number1 * number2
print(f'{number1} * {number2} is {mul}')

# Division: Two integers can be divided using the / sign
div = number3 / number1
# Remember the answer is a float too
print(f'{number3} / {number1} is {div}')

# Remainder: The remainder left when a number is divided by another number can be found using % sign
rem = number3 % 11
# Gives the remainder when number3 is divided by 11
print(f'{number3} % 11 is {rem}')

# Power: A float can be raised to a power using ** operator
pow = number1 ** 2
# Returns number1 to the power of 2
print(f'{number1} to the power 2 is {pow}')


# Printing and formatting floats

# The number of decimals positions printed while printing a float can be controlled in python
number5 = 1.23456789
# We can use two methods:
# 1) The newer fstrings (Recommended)
# Format: {variable:.nf} where n is the number of decimals to be printed
print(f"{number5:.2f} is {number5} in two decimals using f-string")

# 2) Using the older format()
# format feeds each of the parameters passed to it into the curly braces sequentially within a string
print("{:.2f} is {} in two decimals using format".format(number5, number5))

# ------------------------------------------------------------------------------------------------------------------
# Challenge 1: Declare two floats and find the sum, difference, product, quotient and remainder of the two numbers
# ------------------------------------------------------------------------------------------------------------------

# Add your code here

# ----------------------------------------
# Challenge 2: Find the square root of 121
# ----------------------------------------

# Add your code here
