# ------------------------------------------------------------------------------------
# Tutorial: Lets learn how to use if else
# ------------------------------------------------------------------------------------

# For this example we are programming a game that uses lives,
# if a user runs out of lives the program will display a game
# over message.

lives = 0

if lives == 0:         # the variable lives is equal to 0.
    print("Game Over.")
elif lives != 0:       # the variable lives is not equal to 0.
    print("Ha Ha Ha, Staying Alive.")

# For example if we want play a game that is rated 12 years and up
# Lets write a program to check if you can play that game.

age = 13

if age >= 12:
    print("Yes, you can play that game.")
else:
    print("Lets find a better game for you.")


# We can also use elif do a chain of conditions
# like this:

if age < 18:
    print("Can't join army")
elif age > 35:
    print("Can't join army")
else:
    print("Can join army!")

# ------------------------------------------------------------------------------------
# Challenge: Using your knowledge of operators, write two conditions where it
# says "replace-me", to check if your car is going below speed limit and above
# the minimum speed for the street.
# ------------------------------------------------------------------------------------

street_max_speed = 100
street_min_speed = 50
car_speed = 70

if "replace_me":
    print("Lower your speed or you will be penalized")
elif "replace_me":
    print("You should get a higher speed")
else:
    print("Ok, you are in a good speed to travel")
