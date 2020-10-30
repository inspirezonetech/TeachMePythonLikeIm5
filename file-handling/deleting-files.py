# ------------------------------------------------------------------------------------
#    Tutorial: Receives a file name from a user and deletes it
# ------------------------------------------------------------------------------------

import os

def delete_file(filename):
    try:
        os.remove(filename)  # deletes filename
        print(f'{filename} has been deleted')  # prints out success message
    except OSError:
        print('No such file in directory!')  # prints error message when file not found

def main():
    filename = None
    try:
        # get the filename from the user
        filename = input('Please enter name (with type) of the file you would like to remove: ')
    except EOFError:
        return filename

    # call delete function from above and pass in the filename
    delete_file(filename)

if __name__ == '__main__':
    main()


# ------------------------------------------------------------------------------------
#   Challenge: Delete a specific file in directory
# ------------------------------------------------------------------------------------
