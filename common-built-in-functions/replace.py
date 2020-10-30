# ------------------------------------------------------------------------------------
# Tutorial: 
# --> The replace method replaces a specified string with another specified string.
# Syntax: 
# --> string.replace(oldvalue, newvalue, count)
# Params:
# --> oldvalue: Required. The string to replace (str)
# --> newvalue: Required. The string to replace the old value with (str)
# --> count: Optional. How many occurrences of the old value you want to replace (int). 
#                      All if not specified
# Returns:
# --> A copy of the string where the occurrence of a substring is replaced with another substring.
# ------------------------------------------------------------------------------------

############### Example 1. ###############
# Replace all occurences of "dog" with "cat" #

dog_txt = "I always wanted a dog! My dog is awsome :) My dog\'s name is Taco"
cat_txt = dog_txt.replace("dog", "cat")

print("\nExample 1. - Replace all occurences of \"dog\" with \"cat\"")
print(f'Old String: {dog_txt}')
print(f'New String: {cat_txt}')


############### Example 2. ###############
# Replace the two first occurences of "dog" with "cat" #

dog_txt = "I always wanted a dog! My dog is awsome :) My dog\'s name is Taco"
cat_txt = dog_txt.replace("dog", "cat", 2)

print("\nExample 2. - Replace all occurences of \"dog\" with \"cat\"")
print(f'Old String: {dog_txt}')
print(f'New String: {cat_txt}\n')

# ------------------------------------------------------------------------------------
# Challenge: 
# 1. From the string "Teach me Python like Im 5" produce the string "Teach me Java like Im 10".
# 2. From the string "Im 10 years old" produce the string "How old are you?".
# ------------------------------------------------------------------------------------
