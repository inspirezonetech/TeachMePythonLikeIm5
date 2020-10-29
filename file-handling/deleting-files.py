# ------------------------------------------------------------------------------------
# Tutorial: Receives a file name from a user and deletes it
# ------------------------------------------------------------------------------------
import os

def delete (filename):
    try:
        os.remove(filename) #deletes filename
        print(f"{filename} has been deleted") #prints out success message
    except OSError:
        print("No such file in directory!")

def main():
    #get the filename from the user
    filename = input("Please enter name (with type) of the file you would like to remove: ")
    #call delete function from above and pass in the filename
    delete(filename)

if __name__=="__main__":
    main()

# ------------------------------------------------------------------------------------
# Challenge: list challenges to be completed here. minimum of one challenge per tutorial
# ------------------------------------------------------------------------------------
