# ------------------------------------------------------------------------------------
# Tutorial: Learn how to use Dictionaries in Python
# ------------------------------------------------------------------------------------

# Dictionaries are a collection of key-value pairs.
# Keys can only appear once in a dictionary but can be of any type.
# Dictionaries are unordered.
# Values can appear in any number of keys.
# Keys can be of almost any type, values can be of any type.

# Defining a dictionary
# Dictionaries are assigned using a pair of curly brackets.
# Key pair values are assigned within the curly brackets with a : between the key and value
# Each pair is separated by a comma
my_dict = {
    'my_key': 'my value',
    'your_key': 42,
    5: 10,
    'speed': 20.0,
}

# Assigning key-value pairs
# Adding key pairs to an existing dictionary
my_dict['their_key'] = 3.142

# Retreiving a value
retrieved = my_dict['my_key']
print("Value of 'my_key': " + str(retrieved))  # Should print "Value of 'my_key': my value"

retrieved = my_dict.get('your_key')
print("Value of 'your_key': " + str(retrieved))  # Should print "Value of 'your_key': 42"

# With either of the above options Python will throw a key error if the key doesn't exist.
# To fix this dictionary.get() can be used to return a default value if no key exists
retrieved = my_dict.get('non_existent_key', 'Not here.')
print("Value of 'non_existent_key': " + str(retrieved))  # Should print "Value of 'non_existent_key' not here"
print("")

# ------------------------------------------------------------------------------------
# Challenge: Create a dictionary called person.
# The person dictionary should contain the following keys:
# name, height, age
# With the following values:
# 'Sally', 154.9, 15
# Add a key called occupation with value 'student'
# Update the value of age to 18
# Remember to uncomment the print lines
# You should see the output
# Person is called Sally
# Person is 18
# Person is 154.9cm
# Person is student
# ------------------------------------------------------------------------------------

# Define person dictionary here

# Add occupation key here

# Increase the age to 18 here

# Uncomment the lines below once you have completed the challenge
# print("Person is called " + str(person.get("name", "Unnamed")))
# print("Person is " + str(person.get("age", "Ageless")))
# print("Person is " + str(person.get("height", "Tiny")) + "cm")
# print("Person is " + str(person.get("occupation", "Unemployed")))
