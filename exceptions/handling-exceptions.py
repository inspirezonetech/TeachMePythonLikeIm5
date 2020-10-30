# ------------------------------------------------------------------------------------
# Tutorial: Handling exceptions in python

# ------------------------------------------------------------------------------------

# You can handle exceptions in a try / except blocks
# The program executes the code in the try block,
# if something goes wrong an exception is raised
# It will be handled by the except block,
# if not the except section will be ignored.

a = 2

while a > 0:
    try:
        a = a - 1
        print("Working!!")
        if a == 0:
            # Here a custom exception is raised if a is equal to 0
            raise ValueError("a cannot be 0")
    except ValueError:
        print('Something went wrong')
        raise

# ------------------------------------------------------------------------------------
# Challenge: Create a try / except block and raise a custom exception when the value received is not a number
# ------------------------------------------------------------------------------------
