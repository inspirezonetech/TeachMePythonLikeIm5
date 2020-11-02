# ------------------------------------------------------------------------------------
# Tutorial: Importing Modules in Python
# ------------------------------------------------------------------------------------

# The file "calculator.py" which is located in the same directory as this file is an example of a module

# In this line you import the module,
# With the keyword import and the name of your module
import calculator

a = 2
b = 4

# Here we are calling the function inside the module to get the result
# Of the sum of number a and b
result_sum = calculator.sum_two_numbers(a, b)

# Here we are calling the function inside the module to get the result
# Of the multiplication of number a and b
result_multiplication = calculator.multiply_two_numbers(a, b)

print(result_sum)

print(result_multiplication)

# ------------------------------------------------------------------------------------
# Challenge: (Edits needed to "calculator.py" which is located in the same directory as this file)
# Add to the "calculator.py" module two more functions: divide_two_numbers, subtract_two_numbers.
# Then call the new functions, Passing in two integers and print the result
# ------------------------------------------------------------------------------------

# Here call the divide_two_numbers function you created in "calculator.py"


# Here call the subtract_two_numbers function you created in "calculator.py"
