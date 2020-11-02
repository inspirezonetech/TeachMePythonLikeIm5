# ------------------------------------------------------------------------------------
# Tutorial: Learn how to use Dictionaries in Python
# ------------------------------------------------------------------------------------

# Defining a more advanced dictionary
# You can define an empty dictionary by leaving the space between the curly brackets blank
my_dict = {}

# As stated in the basic tutorial values can be of any type. This includes lists and tuples
my_dict['some_collection'] = [5, 6, 7, 8]
my_dict['tuple_trouble'] = ('bread', 'eggs', 'milk',)

# To access the value of a list or tuple stored in the dictionary you can use
# dict[key][index]
print("Value of first element of some_collection: " + str(my_dict['some_collection'][0]))
print("Value of third element of tuple_trouble: " + str(my_dict['tuple_trouble'][2]))
print("")

# They can even be other dictionaries
my_dict['some_child'] = {
    'name': 'Jeremy',
    'sibling': 'Beth',
    'occupation': 'child',
}
# To retrieve the name of some_child use dict[key][key]
print("some_child name is " + str(my_dict['some_child']['name']))
print("")

# Checking if a key exists
if 'my_key' in my_dict.keys():  # dict.keys() returns a list of all keys in the dictionary
    print("Key exists\n")

# How to remove a key
del my_dict['some_child']  # This will throw an error if the key doesn't exist
# A better approach would be to check if the key exists first using the above method
if 'some_child' in my_dict.keys():
    del my_dict['some_child']
    print("Key removed\n")  # This will not be printed as we already deleted the key with del
else:
    print("Can't delete key, it doesn't exist\n")

# To remove a key and retrieve its value you can use dictionary.pop()
# Using the optional second argument for pop will prevent it throwing a key error if the key doesn't exist
fred = my_dict.pop('fred', None)  # Returns the value of the removed key or None if the key doesn't exist
print("Fred is " + str(fred))  # Will print 'Fred is None'

# Count the number of items (key-value pairs) in the dictionary
size = len(my_dict)
print("\nSize of my_dict: " + str(size))  # Should print 2
print("")

# You can add one dictionary to another using dictionary.update()
new_dict = {
    'address': '221b Baker Street',
    'owner': 'Holmes',
}
my_dict.update(new_dict)
print("Updated dictionary " + str(my_dict))

# ------------------------------------------------------------------------------------
# Challenge: You are in charge of creating an RPG character for a game.
# Add a key to to the player dictionary called inventory and assign it an array of items
# 'sword', 'waterskin', 'bedroll'
# Define a new dictionary called stats with key pairs as below
# 'hp': 10, 'dexterity': 1, 'strength': 3
# and update the player dictionary with it.
# Call use_item() with the id for 'waterskin'
# It should print "Using item waterskin"
# ------------------------------------------------------------------------------------

def use_item(id):
    inv = player.get('inventory', [])
    if len(inv) > 0:
        print("Using item " + str(inv[id]))
    else:
        print("No inventory")  # Your solution is incorrect if you see this line printed

player = {
    'name': 'the hero',
    'level': 10,
    'xp': 3250,
}

# Define and add inventory here

print("\nPlayer dictionary")
print(player)  # Should print "{'name': 'the hero', 'level': 10, 'xp': 3250}""

# Define stats and update player here

print("\nUpdated player dictionary")
print(player)  # Should print "{'name': 'the hero', 'level': 10, 'xp': 3250, 'inventory': ['sword', 'waterskin', 'bedroll'], 'hp': 10, 'dexterity': 1, 'strenth': 3}""

# Call use_item() here
