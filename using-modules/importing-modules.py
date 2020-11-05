# ------------------------------------------------------------------------------------
# Tutorial: importing modules
# ------------------------------------------------------------------------------------
# What is a module ?
# A module is a file which ends by .py. Very simple, you can even create
# yourself a module. The name of the module takes automatically the name of the file.
# It can contain many things (functions, variable ...) you can use everywhere on your project.
# To use a module, you have to import it. We use the keyword "import" + module name.

# Example for one import :
# import os

# But Python have standard so let's do it well...
# Multiple imports, not in the same line :
# import sys
# import warnings

# Specific thing imported from a module we use the keyword "from" :
# from datetime import date
# but we can write that like we see above :
# import datetime.date

# the path is really important, it means date is in the file datetime.py
# Note that all imports must be at the top of the file

# ------------------------------------------------------------------------------------
# Challenge: use the random import
# ------------------------------------------------------------------------------------
# Python has the module random, import it and uncomment the code below to show a
# random number and set your favorite number to show a nice message if it's the
# right number when you execute this file

# favorite_number = 1
# number = random.randint(0, 6)
# if number == favorite_number:
#     print("Yeah, it's your number! Lucky you!")
# else:
#     print('Nope, try again')
