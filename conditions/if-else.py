# ------------------------------------------------------------------------------------
# Tutorial: Lets learn how to use if else
# ------------------------------------------------------------------------------------

# For example if we want go to play a game that is rated for 12+ year old
# Lets so we will build a program to check if you can play that game

age = 13
if age >= 12:
    print("Yes, you can that game.")
else:
    print("Lets find a better game to you.")

# We can also use elif do a chain of conditions
# like this:
age = 18
if age < 18:
    print("Can't join army")
elif age > 35:
    print("Can't join army")
else:
    print("Can join army!")

# ------------------------------------------------------------------------------------
# Challenge: Fix the code below to print truly statements
# Don't change the values, change the ? to right statements
# ------------------------------------------------------------------------------------
street_max_speed = 100
street_min_speed = 100
car_speed = 200

if ? :
    print("Lower your speed or you will be penalized")
elif ? :
    print("You should get a higher speed")
else:
    print("Ok, you are in a good speed to travel")
