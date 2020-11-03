# -----------------------------------------------------
# Tutorial: An explanation of the int(integer) datatype
# -----------------------------------------------------

# In python, numbers without decimals are stored using the int datatype
number1 = 10  # We can directly assign a number to a variable
# We can check the datatype of a variable using the type function. So let's verify if the variable number1 is an int(integer) or not
print("Type of number1 is", type(number1))
# We can see that Python is smart enough to make the variable number as an int. This is called Dynamically typed.

# We can also declare an integer using the int() function
number2 = int(20)
# We can see that the variable number2 is an integer too. This is called Static typed as we are giving the type
print("Type of number2 is", type(number2))

# We can also convert from other datatype to integer using int()
number3 = int("30")
# Python converts the string to an integer.
print("Type of number3 is", type(number3))

# Integers can hold negative numbers too
number4 = -10
print("Type of number4 is", type(number4))


# Operations on int

# Addition: Two integers can be added using the + sign
sum = number1 + number2
print(f'{number1} + {number2} is {sum}')

# Subtraction: Integers can be subtracted using the - sign
diff = number3 - number2
print(f'{number3} - {number2} is {diff}')

# Multiplication: Two integers can be multiplied using the * sign
mul = number1 * number2
print(f'{number1} * {number2} is {mul}')

# Division: Two integers can be divided using the / sign
div = number3 / number1
# Remember the answer is a decimal even if the numbers are perfectly divisible
print(f'{number3} / {number1} is {div}')

# Remainder: The remainder left when a number is divided by another number can be found using % sign
rem = number3 % 11
# Gives the remainder when number3 is divided by 11
print(f'{number3} % 11 is {rem}')

# Power: An integer can be raised to a power using ** operator
pow = number1 ** 2
# Returns number1 to the power of 2
print(f'{number1} to the power 2 is {pow}')

# ------------------------------------------------------------------------------------------------------------------
# Challenge 1: Declare two integers and find the sum, difference, product, quotient and remainder of the two numbers
# ------------------------------------------------------------------------------------------------------------------

# Add your code here

# --------------------------------
# Challenge 2: Find the cube of 39
# --------------------------------

# Add your code here
