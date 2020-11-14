# ------------------------------------------------------------------------------------
# Tutorial: brief description of tutorial content
# ------------------------------------------------------------------------------------
# Boolean variables are defined by the True and False keywords
# eg: a = True
# We can check type of variables by printing : type(var_name)
# If it is of type boolean it will return : <class 'bool'>
# bool() method can be used to convert value to boolean value
# It returns True if the parameter or value passed is True
# It returns False if the parameter or value passed is False with some exceptions such as
# If False value is passed, None is passed, an empty sequence is passed such as (), [], ”, etc, or if Zero is passed in any numeric type such as 0, 0.0, etc.

# Code here explaining concept with comments to guide
def Boolean():
    # Returns True as x is True
    x = True
    print(bool(x))
    # Returns False as x is False
    x = False
    print(bool(x))
    # Returns False as x is not equal to y
    x = 15
    y = 18
    print(bool(x == y))
    # Returns False as x is None
    x = None
    print(bool(x))
    # Returns False as x is an empty sequence
    x = ()
    print(bool(x))
    # Returns False as x is an emty mapping
    x = []
    print(bool(x))
    # Returns False as x is 0
    x = 0.00
    print(bool(x))
    # Returns True as x is a non empty string
    x = 'This is Boolean Tutorial'
    print(bool(x))

Boolean()

def Challenge(arg1, arg2, arg3):
    print("Challenge:")
    print(bool(arg1))
    print(bool(arg2))
    print(bool(arg3))

Challenge([], 125, True)

# --------------------------------------CHALLENGE----------------------------------------------
# Challenge: call the Challege function and pass the values '0.00', '{1, 341, 56}' and 'False' to the function
