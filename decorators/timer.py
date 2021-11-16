# ------------------------------------------------------------------------------------
# Tutorial: Implementation of decorator in Python.
# ------------------------------------------------------------------------------------

import time

# defining the decorator timer
def timer(func):
    # wrapper function taking arbitary arguments
    def wrapper(*args, **kwargs):
        # storing the current time.
        start_time = time.time()
        # calling func passed in the timer function.
        func(*args, **kwargs)
        # displaying the time it takes to completely run the func.
        print("Function took : ", time.time() - start_time, "seconds.")
    # returning the wrapper function.
    return wrapper

# using decorator timer
@timer
# defining a function to decorate with timer.
def run():
    for i in range(10):
        print(i)

# calling the function which is decorated with timer.
run()

# ------------------------------------------------------------------------------------
# Challenge: Create a decorator to wrap a function and print "START" before the function call and print "END" after the function executes successfully.
# ------------------------------------------------------------------------------------
