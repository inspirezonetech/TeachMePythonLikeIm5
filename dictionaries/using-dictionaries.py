# ------------------------------------------------------------------------------------
# Tutorial: Learn how to use Dictionaries in Python
# ------------------------------------------------------------------------------------

# Dictionaries are a collection of key-value pairs.
# Keys can only appear once in a dictionary but can be of any type.
# Dictionaries are unordered
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
}

# Adding key pairs to an existing dictionary
my_dict['their_key'] = 3.142

# This can also be used to reassign the value of a key
my_dict['their_key'] = 6.284

# As stated before values can be of any type. This includes lists and tuples
my_dict['some_collection'] = [5, 6, 7, 8]
my_dict['tuple_trouble'] = ('bread', 'eggs', 'milk',)

# They can even be other dictionaries
my_dict['some_child'] = {
    'name': 'Jeremy',
    'sibling': 'Beth',
    'occupation': 'child',
}

# Checking if a key exists
if 'my_key' in my_dict.keys():
    print("Key exists\n")

# Removing a key pair
del my_dict['their_key']  # This will throw an error if the key doesn't exist
# A better approach would be to check if the key exists first using the above method
if 'their_key' in my_dict.keys():
    del my_dict['their_key']
    print("Key removed\n")  # This will not be printed as we already deleted the key with del

# Another approach is to pop() the key.
# pop() will remove a key pair and return the value.
# Using the optional second argument for pop will prevent it throwing a key error if the key doesn't exist
fred = my_dict.pop('fred', None)  # Returns the value of the removed key or None if the key doesn't exist
print("Fred is " + str(fred))  # Will print 'Fred is None'
print("")

# Retreiving a value
retrieved = my_dict['my_key']
print("Value of 'my_key': " + str(retrieved))  # Should print "Value of 'my_key': my value"

retrieved = my_dict.get('your_key')
print("Value of 'your_key': " + str(retrieved))  # Should print "Value of 'your_key': 42"

# dictionary.get() can be used to return a default value if no key exists
retrieved = my_dict.get('non_existent_key', 'Not here.')
print("Value of 'non_existent_key': " + str(retrieved))  # Should print "Value of 'non_existent_key' not here"

# Count the number of items (key-value pairs) in the dictionary
size = len(my_dict)
print("\nSize of my_dict: " + str(size))  # Should print 6
print("")

# You can add the data from one dictionary to another using dict.update()
separate_dict = {'hi': 'beep'}
my_dict.update(separate_dict)
print("\nUpdated dictionary")
print(my_dict)
print("")

# To return a list of all keys use dict.keys(). This can be useful for iterating over the data.
keys = my_dict.keys()
for key in keys:
    print("Value for key " + str(key) + " is " + str(my_dict[key]))

# To return a list of all values use dict.values() (This will be useful for the advanced challenge).
for value in my_dict.values():
    if value == 10:
        print("Found the required value")  # There is a key (5) with value 10 so this line will print

# To return a list of all key-value pairs use dict.items().
# Each item in the list will be returned as a tuple containing key and value like so (key, value,)
for item in my_dict.items():
    if item[0] == 5:
        print("Found the required key with value " + str(item[1]))

# It can be useful to increment a value even if the key doesn't exist yet as it will save an if/else.
# (This may be useful for the advanced challenge)
# The following line returns the value of the key if it exists or 0. It then adds 1 to the returned value
# and assigns the value to the key.
my_dict['count'] = my_dict.get('count', 0) + 1

# ------------------------------------------------------------------------------------
# Challenge: Create a dictionary called person.
# The person dictionary should contain the following keys:
# name, height, age
# With the following value types:
# string, float, int
# Fill in the birthday function so that the value of age is incremented by 1 each time
# OPTIONAL: Add a congratulatory print statement to the end of birthday if age equals 18
# ------------------------------------------------------------------------------------

# Define person dictionary here

def birthday(person):
    pass  # Remove this line and replace it with the correct code as per the challenge

# print(person.get("age", "Ageless"))  # Uncomment the print statement once you have completed the challenge.

# ------------------------------------------------------------------------------------
# Challenge: ADVANCED You are in charge of the census data for family size.
# Below is a dictionary containing the surnames of various families along with the
# number of children in those families.
# You are interested in finding which is the most common number of children.
# HINT: You will need to know about loops as well to complete this challenge.
# Define a dictionary called counts with the number of children as the keys and increment
# the value each time the key is found.
# ------------------------------------------------------------------------------------

census_data = {
    'Hall': 3,
    'Brown': 5,
    'Farmer': 2,
    'Baggins': 1,
    'Fry': 3,
    'Cameron': 3,
    'Andrews': 2,
    'Jeffries': 3,
}

# Enter your solution here

# This method is beyond the scope of the tutorial, it is here for interest and to help check the outcome of the challenge.
def get_most_common_child_count(child_counts):
    sorted_children = sorted(child_counts.items(), key=lambda x: x[1], reverse=True)
    print("The most common number of children is %s with %s families having this many" % (sorted_children[0][0], sorted_children[0][1]))

# Uncomment the line below once you have completed the challenge
# get_most_common_child_count(counts)  # Should print 'The most common number of children is 3 with 4 families having this many'
