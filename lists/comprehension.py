# ------------------------------------------------------------------------------------
# Tutorial: List comprehension
# ------------------------------------------------------------------------------------
# It's a Python feature to iterate and create a list from some other list in a
# shorter and declarative way than loops.


# In general there is a very common for loop structure that looks like this:
for_loop_squares = []

for i in range(10):
    for_loop_squares.append(i * i)

print(for_loop_squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# With list comprehension you can do the exact same thing:
comprehension_squares = [x * x for x in range(10)]

print(comprehension_squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# You can even add conditionals to the list comprehension:
comprehension_even_squares_numbers = [x * x for x in range(10) if x % 2 == 0]

print(comprehension_even_squares_numbers)  # [0, 4, 16, 36, 64]


# But if you can do if/else logic, you need to do:
comprehension_even_squares_numbers_and_odd_numbers_is_zero = [x * x if x % 2 == 0 else 0 for x in range(10)]

print(comprehension_even_squares_numbers_and_odd_numbers_is_zero)  # [0, 0, 4, 0, 16, 0, 36, 0, 64, 0]


# As you can see, the basic format of a list comprehension is like:
# new_list = [expression for member in iterable]

# With only one condition
# new_list = [expression for member in iterable if condition]

# With if/else logic:
# new_list = [expression if condition else other_expression for x in sequence]


# ------------------------------------------------------------------------------------
# Challenge: FIZZBUZZ
# Create a list comprehesion that returns the numbers from 0 to 100 but:
#   1 -. if the number is divisible by 3 and 5, append to the list the word "FizzBuzz"
#   3 -. else, append to the list the number
# ------------------------------------------------------------------------------------
