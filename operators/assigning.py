# ------------------------------------------------------------------------------------
# Tutorial: Assignment operators
# ------------------------------------------------------------------------------------

# The assignment operators are the most important for any program, as they are the way
# to store a value we want to work with. Said value will be stored in a variable where
# we will be able to perform read and write operations.

# The following lines shows the most basic assignment:
var = 1
# Now the variable called `var` contains the value `1` and allows us to perform
# actions with it, such as performing arithmetic operations or comparisons:
print(var + 4)  # 5
print(var == 1)  # True

# The expression on the right of the assignment will be evaluated before assigning the
# value to the target. That means that we can have the variable on both sides of the
# statement, because it's value will be first read (right) and later updated (left).
# For example:
var = var + 2
# In this case, `var` has an original value of 1 (var = 1). In the above statement, the
# expression is first calculated (1 + 2) and the result (3) is then assigned to `var`.
print(var)  # 3

# In this aspect, there are more assignment operators that pretend to shorten a small
# operation on the variable and then an assignment to itself. As an example, the
# following line will do the same as the one above:
var += 2  # var = var + 2
# These kind of assignments always add the target variable on the left side of the
# operation.

# There are a certain amount of operations with this kind of shortcut.
# Arithmetic assignments:
var += 10   # var = var + 10
var -= 10   # var = var - 10
var *= 10   # var = var * 10
var /= 10   # var = var / 10
var %= 10   # var = var % 10
var //= 10  # var = var // 10
var **= 10  # var = var ** 10
# Bitwise assignments:
var &= 10   # var = var & 10
var |= 10   # var = var | 10
var ^= 10   # var = var ^ 10
var >>= 10  # var = var >> 10
var <<= 10  # var = var << 10
# The variable is always the last part of the expression to be evaluated. That means
# that if on the right side there's a more complex operation, the operation on the
# variable will not be done after that is complete. For example:
var = 2
var *= 3 + 2
# The command above equals to `var * (3 + 2)` and not to `var * 3 + 2`. The assignment
# operator has the least priority of all the operators.


# HONORABLE MENTIONS
# - Not strongly typed: var can have different types
# - Multiple assignments inline: a = b = c
# - walrus a := exp
# - Unpacking: a, b = 1, 2

# ------------------------------------------------------------------------------------
# Challenge: list challenges to be completed here. minimum of one challenge per tutorial
# ------------------------------------------------------------------------------------
