# ------------------------------------------------------------------------------------
# Tutorial: Learn how to iterate over dictionaries
# ------------------------------------------------------------------------------------

my_dict = {
    'first_key': 1,
    'second_key': 'second value',
    'third_key': 3.0,
    'fourth_key': {
        'sub_key1': 'sub_value1',
        'sub_key2': 2,
        'sub_key3': 9.0,
    }
}

# dictionary.keys() will return a list of all the keys in the dictionary.
# If you want to iterate over all keys you can use a for loop
for key in my_dict.keys():
    print("Key: " + str(key))
print("")

# You can then pass the value of key back into the dictionary to retrieve the value
for key in my_dict.keys():
    print(str(my_dict[key]))
print("")

# dictionary.values() will return a list of all the values in the dictionary
for value in my_dict.values():
    print("Value: " + str(value))
print("")

# dictionary.items() will return a list of all the key-value pairs in the dictionary
# The items in the list will be tuples in the form (key, value,)
for item in my_dict.items():
    print("Key: " + str(item[0]) + "\t| Value: " + str(item[1]))
print("")

# As you might expect all the above methods can be applied to values that are dictionaries
print("Iterating over a sub dictionary")
for item in my_dict['fourth_key'].items():
    print("Key: " + str(item[0]) + " | Value: " + str(item[1]))
print("")

# As stated in using-dictionaries-basic.py keys can be of almost any type. However one type
# that cannot be a key is dictionary.
# For fun let's create a new dictionary. We will set the keys to the values of my_dict
# and the values to the keys of my_dict.
# First we must remove fourth_dict from the dictionary otherwise we will receive a TypeError.
del my_dict['fourth_key']

swapped_dict = {}
for item in my_dict.items():
    swapped_dict[item[1]] = item[0]
print("Swapped dictionary: ")
print(swapped_dict)

# ------------------------------------------------------------------------------------
# Challenge: You are in charge of restocking at the grocery store.
# Stock is stored by category: fruit, vegetable, bathroom
# Look through all the category keys.
# Look through all the items within the category.
# If an item has a value of 0 (out of stock) add it as a key to
# the restock dictionary and set the value to 5
# HINT: It helps to think of each category as its own dictionary
# HINT: You should be able to do this with 2 nested loops
# ------------------------------------------------------------------------------------

stock = {
    'fruit': {
        'pineapple': 5,
        'pear': 0,
    },
    'vegetable': {
        'carrot': 0,
        'radish': 10,
    },
    'bathroom': {
        'soap': 3,
        'shampoo': 0,
    },
}

restock = {}

# Type your solution here

print("\nItems to restock")
print(restock)  # Once you've completed the challenge should print "{'pear': 5, 'carrot': 5, 'shampoo': 5}"
