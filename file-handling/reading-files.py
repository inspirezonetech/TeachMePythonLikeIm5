# -------------------------------------------------------------------------------------------------
# Tutorial: Receives a file name from the user, reads and then displays the contents to the console
# -------------------------------------------------------------------------------------------------

def read_file(filename):
    try:
        fr = open(filename, mode="r")  # Creates a file pointer to the given file name and the mode 'r' opens the file in read mode
        fcontents = fr.read()  # Reads all the contents of the file into the variable fcontents as a single string
        print(f"The contents of the file {filename}:")
        print(fcontents)
    except FileNotFoundError:
        print('File not found!')

def main():
    filename = None
    try:
        # get the filename from the user
        filename = input('Please enter name of the file you would like to read: ')
    except EOFError:
        return filename

    # call read_file function from above and pass in the filename
    read_file(filename)

if __name__ == '__main__':
    main()

# ---------------------------------------------------------------------------------------------------------------------
# Challenge 1: Create a file in the directory with some contents. Run the program and display the contents of that file
# ---------------------------------------------------------------------------------------------------------------------
