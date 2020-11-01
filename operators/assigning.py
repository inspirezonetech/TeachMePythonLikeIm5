# -----------------------------------------------------------------------------
# Tutorial: Assignment operators
# -----------------------------------------------------------------------------

# The assignment operators are the most important for any program, as they are
# the way to store a value we want to work with. Said value will be stored in a
# variable where we will be able to perform read and write operations.

# The following lines shows the most basic assignment:
var = 1
# Now the variable called `var` contains the value `1` and allows us to perform
# actions with it, such as performing arithmetic operations or comparisons:
print(var + 4)  # 5
print(var == 1)  # True

# The expression on the right of the assignment will be evaluated before
# assigning the value to the target. That means that we can have the variable
# on both sides of the statement, because it's value will be first read (right)
# and later updated (left). For example:
var = var + 2
# In this case, `var` has an original value of 1 (var = 1). In the above
# statement, the expression is first calculated (1 + 2) and the result (3) is
# then assigned to `var`.
print(var)  # 3


# ARITHMETIC AND BITWISE ASSIGNMENTS

# There are more assignment operators that intend to shorten a small operation
# on the variable and then an assignment to itself. As an example, the
# following line will do the same as the one above:
var += 2  # var = var + 2
# These kind of assignments always add the target variable on the left side of
# the operation.

# There are a certain amount of operations with this kind of shortcut.
# Arithmetic assignments:
var += 10   # var = var + 10
var -= 10   # var = var - 10
var *= 10   # var = var * 10
var /= 10   # var = var / 10
var %= 10   # var = var % 10
var //= 10  # var = var // 10
var **= 10  # var = var ** 10

var = 1
# Bitwise assignments:
var &= 10   # var = var & 10
var |= 10   # var = var | 10
var ^= 10   # var = var ^ 10
var >>= 10  # var = var >> 10
var <<= 10  # var = var << 10
# The variable is always the last part of the expression to be evaluated. That
# means that if on the right side there's an operation, the operation on the
# variable will not be done after that is complete. For example:
var = 2
var *= 3 + 2
# The command above equals to `var * (3 + 2)` and not to `var * 3 + 2`. The
# assignment operator has the least priority of all the operators.


# TYPING IN ASSIGNMENTS

# In Python, variables are not strongly typed, which means that they can change
# their type with every assignment.
var = 1
print(type(var))  # <class 'int'>
var = 'string'
print(type(var))  # <class 'str'>


# CHAINED ASSIGNMENT

# On simple assignments `=`, multiple variables can be assigned the same
# value in the same line, for instance:
var = var2 = 3
print(var, var2)  # 3 3


# ASSIGNING TUPLES

# When working with tuples it's important to know that its values can be
# unpacked in different variables with an assignment:
tup = (1, 2, 3)
a, b, c = tup
print(tup[1])  # 2
print(b)  # 2
# Of course, this can be used to assign different values to different values
# on the same line, such as:
value1, value2 = 10, 2
print(value1)  # 10
print(value2)  # 2


# WALRUS OPERATOR

# On Python 3.8 the walrus operator `:=` was introduced. Said operator allows
# to perform an assignment during the evaluation an expression.
# This allows us to, instead of performing an operation, assigning it to a
# variable (to later reuse it) and evaluating the result in 2 different lines,
# it can be done in one.
# Without the walrus operator:
result_no_walrus = value1 + value2
if result_no_walrus > 10:
    print(result_no_walrus)  # 12
# With the walrus operator:
if (result_with_walrus := value1 + value2) > 10:
    print(result_with_walrus)  # 12

# -----------------------------------------------------------------------------
# Challenge: Starting with the tuple (5, 10, 15) get the result of adding each
# value multiplied by its position in a single variable ONLY using assignment
# operators. (That's to say: 5 * 1 + 10 * 2 + 15 * 3)
# -----------------------------------------------------------------------------
