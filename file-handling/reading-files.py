# -------------------------------------------------------------------------------------------------
# Tutorial: Receives a file name from the user, reads and then displays the contents to the console
# -------------------------------------------------------------------------------------------------

# Taking the file we would like to read (Similar to selecting a book you want to read)
# Make sure you give the full path in case the file is not present in the same location as the program
filename = input("Enter the file name you would like to read: ")

# Since we know which file to read let's open it first (We have to open the book first so that we can read)
fread = open(filename, mode="r")  # Here the r specifies we want to read the file

# Now since we have the file open we can read it (Once our book is open we can start reading from the book)
fcontents = fread.read()  # Reads and saves all the contents into the variable fcontents

# As we have read from the file we check out what's present in the file
print(fcontents)

# -----------------------------------------------------------------------------------------------------------------------------------------------
# Challenge: Create a file and add some content into the file. Check whether the output from the program matches the content you have in the file
# -----------------------------------------------------------------------------------------------------------------------------------------------
