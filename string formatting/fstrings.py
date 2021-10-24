# ------------------------------------------------------------------------------------
# Tutorial on f-strings
# Using f-strings is a simple and fast method for String formatting

# ------------------------------------------------------------------------------------

# # Syntax of f-strings:
# We start the string with the keyword f, followed by our string in double quotes and {} is used as a placeholders for the values involved in the formatting.


# The following example makes it clearer:
name = "John"
age = 17
print(f"I am {name} and I am {age} years old")

# Output- I am John and I am 17 years old

# Note that F(in capitals) also works


# Using multi-line f-strings:
name = 'John'
age = 32
occupation = 'Web developer'

msg = (
    f'Name: {name}\n'
    f'Age: {age}\n'
    f'Occupation: {occupation}'
)
print(msg)

# Output:
# Name: John
# Age: 32
# Occupation: Web developer

# ------------------------------------------------------------------------------------
# Challenge:
# Using f-strings print the following:
# Hi, I am <name>, my hobby is <hobby>, and I'm from <location>
# name, hobby and location will be inputs from the user
# Do the same for a multi-line output.
# ------------------------------------------------------------------------------------
