# ------------------------------------------------------------------------------------
# Tutorial: Learn how and when to use virtual environments
# ------------------------------------------------------------------------------------

# What is a Virtual Environment
# A virtual environment allows you to create a directory on your computer which has
# a separate set of dependencies and settings from the rest of your computer.
# For example say you have one project that uses PIL 8.0.1 and another that uses PIL 7.1.0
# you will have to keep reinstalling different versions as you work across the projects.
# With virtual environments you can install one version of PIL in one project directory and
# the other version in the other directory and each will run with the correct dependencies each time.
# As long as the virtual environment is active it will use the correct dependencies for the project.

# How to install Python Virtual Environment System
# In the command line type:
# pip install virtualenv
# For more information on pip see using-modules/installing-with-pip.py

# How to Create a Virtual Environment
# To create a virtual environment run the following command:
# python -m venv /path/to/<environment_name>

# How to Start the Virtual Environment
# Navigate to the root of your project and in Windows type:
# <virtualenv_name>/Scripts/activate
# In most Unix based operating systems (including MacOS) type:
# source <virtualenv_name>/bin/activate
# Once started you will see a little (<virtualenvironment_name>) in your command prompt.
# Any Python program you run or dependency you install while the virtual environment is active
# will use the dependencies and settings defined in that virtual environment.
# You can run multiple virtual environments from multiple command line instances.

# How to Stop the Virtual Environment
# From the active virtual environment instance run the command:
# deactivate

# ------------------------------------------------------------------------------------
# Challenge: Create a virtual environment within /using-modules named ienv
# E.g. TeachMePythonLikeIm5/using-modules/ienv
# Before going further check that pip is installed by running:
# pip --version
# If you see a message similar to pip 18.1 from [installation_path] (python version)
# you can continue. If not, install pip by running:
# python get-pip.py
# For more information on pip see /using-modules/installing-with-pip.py
#
# With pip installed:
# Start the virtual environment.
# While the virtual environment is active run the command
# pip install pillow==8.0.0
# then run this file:
# python using-virtual-environments.py
# Once you have seen that the output is correct (it should print 8.0.0) deactivate the
# virtual environment.
# OPTIONAL: Re-run the script with the virtual environment deactivated. If pillow has not
# previously been installed you will receive an import error (this is OK for the challenge).
# If pillow has been installed on your computer before it will print the version number
# of the previously installed pillow.
# ------------------------------------------------------------------------------------

from PIL import Image
print(Image.__version__)
