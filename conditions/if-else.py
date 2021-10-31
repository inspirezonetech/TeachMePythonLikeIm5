# ------------------------------------------------------------------------------------
# Tutorial: Lets learn how to use if else
# ------------------------------------------------------------------------------------

# For example if we want go to play a game that is rated for 12+ year old
# Lets so we will build a program to check if you can play that game

# Example using >= operator
age = 13
if age >= 12:
    print("Yes, you can play that game.")
else:
    print("Let's find a better game for you.")
    
# Example using == operator    
age = 17
if age == 16:
    print("You can have your Sweet 16 party this year.")
else:
    print("You are either too old or too young for a Sweet 16 party.")

# Example using != operator    
age = 16
if age != 16:
    print("You are either too old or too young for a Sweet 16 party.")
else:
    print("You can have your Sweet 16 party this year.")
    
# We can also use elif do a chain of conditions
# like this:
age = 18
if age < 18:
    print("Can't join army.")
elif age > 35:
    print("Can't join army.")
else:
    print("Can join army!")
    
    
# ------------------------------------------------------------------------------------
# Challenge: Fix the code below to print true statements.
# Don't change the values. Change the replace_me to the correct statements.
# ------------------------------------------------------------------------------------
street_max_speed = 100
street_min_speed = 50
car_speed = 70

replace_me = False
if replace_me:
    print("Lower your speed or you will be penalized")
elif replace_me:
    print("You should get a higher speed")
else:
    print("Ok, you are in a good speed to travel")
