# ------------------------------------------------------------------------------------
# Tutorial: Learn how to use pip package manager for Python
# ------------------------------------------------------------------------------------

# What is pip?
# Pip is the most popular package manager for Python.
# A package manager allows you to quickly find, install and update modules for your python project
# It will handle module dependencies and download additional modules as needed.
# Packages can refer to a module or a collection of related modules.

# Checking if pip is intalled
# pip may be installed on some systems by default. From the command line type:
# pip --version

# If pip is installed you should see a response similar to:
# pip 18.1 from [installation_path] (python version)

# Installing pip
# Python has a built in script designed to fetch and install the pip system.
# From the command line run:
# python get-pip.py
# If you are on windows you may need to change this to python.exe

# Updating pip
# To update pip itself to the latest version you can run
# python -m pip install --upgrade pip

# Installing packages with pip
# Most popular packages can be found in pip.
# They often give you instructions on what command to run to install the package from pip
# To install a package type:
# pip install <package-name>

# Package versions
# pip packages use semantic versioning.
# This is a number like 2.0.0
# Where the first number indicates the major version of the project. If this number changes it means the versions are incompatible with each other
# The second number indicates the minor version. This is used when functionality has been added without breaking compatibility with previous versions
# The third number indicates the patch version. This is used when no functionality has been added but bugs have been fixed.

# Installing a specific version of a package
# pip allows you to install the latest (default) version of a package or request a specific version
# or a version within a range of versions
# pip install <package-name>==0.1.0 # This will install version 0.1.0

# pip install <package-name>~=0.1.0 # This will install the latest version closest to 0.1. For example if 0.1.0 and 0.1.5 both exist it will choose 0.1.5.

# To install a version within a range of acceptable versions:
# pip install <package-name>>=0.1.0<0.2
# This will install a suitable version between 0.1 and less than 0.1.*.
# Wildcard operators can also be used
# pip install <package-name>==0.1.* will install any available version from the same minor version, it should usually be the latest bugfix patch.

# Updating packages with pip
# To update a package to the latest version use the following line:
# pip install <package-name> --upgrade

# ------------------------------------------------------------------------------------
# Challenge: Try to install the pillow package then uncomment all the code below and
# run the file.
# Pillow is a Python fork of the PIL image manipulation library. At time of writing
# The version installed should be around 8.0.1.

# Make sure you run the file from the /using-modules folder otherwise Python won't
# be able to find the image file to edit.
# Upon successfully running the python file you should see a new image in the
# /using-modules folder called inverted.jpg where the colours have been inverted.
# Image source: https://search.creativecommons.org/photos/519f445f-4987-4487-a927-4d7117c53096
# Image license: Public Domain
# ------------------------------------------------------------------------------------

# from PIL import Image
# from PIL import ImageChops

# with Image.open("image.jpg") as im:
#     inverted_img = ImageChops.invert(im)
#     inverted_img.save("inverted.jpg")
