# ------------------------------------------------------------------------------------
# Tutorial: Importing Modules in Python
# ------------------------------------------------------------------------------------

# Create a module in another file with the functions or data you need
# Also you can import modules from other libraries with pip
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
# Challenge: Create a calculator module, with the 4 basics functions 
# sum, multiply, divide, substract
# ------------------------------------------------------------------------------------
