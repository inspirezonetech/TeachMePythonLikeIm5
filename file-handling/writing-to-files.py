# ----------------------------------------------------------------
# Tutorial: Opens/creates a file and writes contents into the file
# ----------------------------------------------------------------

# Select a file name in which you would like to write (Similar to selecting a book you want to write)
# Make sure you give the full path in case the file is not present in the same location as the program
# Unlike during read, if the file doesn't exist Python otself creates the file first and then opens it
# If the file already has some content then Python overwrites it (So be careful when selecting the file)
filename = "Test.txt"  # Give your file name here
# filename = input("Enter the file name you would like to read: ")  # uncomment if you want to give the file name while running

# Since we know which file to write let's open it first (We have to open the book first so that we can write into it)
fwrite = open(filename, mode="w")  # Here the w specifies we want to write new content to the file
# In the above syntax if we give a instead of w then we can append that is insert the content at the end of the file instead of overwriting the file

#Let's give what we want to write into the file
fcontents = f"This is written from my python program into the file {filename}"
# filename = input("Enter the file contents you would like to write into the file: ")  # uncomment if you want to give the file contents while running

# Now since we have the file open and the contents ready, we can start writing onto it (Once our book is open we can start writing in the book)
fwrite.write(fcontents)  # Writes the content stored in fcontents to the file and saves it
print(f"{fcontents} written into the file {filename}")

# It is always a good practice to close the file once we finished working with it
fwrite.close()

# -----------------------------------------------------------------------------------------------------------------------------------
# Challenge: Create a file and add some content into the file using python. Open the file and check if the contents are written to it
# -----------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Challenge 2: In the same file you created in the previous challenge try adding some more content without overwriting what you have already written
# (Hint: Try the a option instead of w)
# --------------------------------------------------------------------------------------------------------------------------------------------------
