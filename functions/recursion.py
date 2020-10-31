def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 20
print("The factorial of", num, "is", factorial(num))