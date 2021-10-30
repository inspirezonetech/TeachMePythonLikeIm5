# ------------------------------------------------------------------------------------------------------------------------------------
# Tutorial: Receives a directory name from the user, scans the directory and then displays the files in the directory to the console
# ------------------------------------------------------------------------------------------------------------------------------------

import os  # This provides functions for interacting with the operating system.

# Taking the directory we would like to scan (Similar to selecting a box of apples and other boxes inside it with name labels)
# Make sure you give the full path in case the directory is not in the same location as the program
directorypath = ""  # Give your directory name/path here
# directorypath = input("Enter the directory name/path you would like to scan: ")  # uncomment if you want to give the directory name while running

try:
    # Since we know which location to scan let's get all the file/folder names in it first (We have to get all the names of apples and boxes)
    directorynames = os.listdir(directorypath)  # We get a list of files/folders names in the location
    for entry in directorynames:  # We iterate through each file/folder inside the given folder name and store the name in the entry variable each time(we store the name of the apple/box each time)
        if os.path.isfile(os.path.join(directorypath, entry)):  # We check whether it is a file or not(Check if it is an apple or box)
            print(entry)  # We print the name if it is a file(Show if it is an apple, so in this way boxes are filtered out.)

except (EOFError, FileNotFoundError):
    print("Directory not found! Please check if the directory exists in the current path or provide the full path.")

# ---------------------------------------------------------------------------------------------------------------------------------
# Challenge: Create a folder/directory and add some files and folders. Change the directoryname in the program and verify the output
# ---------------------------------------------------------------------------------------------------------------------------------
