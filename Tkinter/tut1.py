# ------------------------------------------------------------------------------------
# Tutorial: Here, we would learn how to create simple GUIs with the help of Tkinter
# module in python, which comes pre-istalled with python, so you can directly jump on coding
# to know how to use it

# If you are unfamiliar with what is a GUI, you can check article on realpython.com
# ------------------------------------------------------------------------------------

# Firstly, we would start with how to create a simple tkinter window

    #importing modules first
from tkinter import * #by this you can call all functions of that particular module at single time
root=Tk()     # for versions earlier than python3 , t is in small case in Tk i.e. tk()
root.mainloop()  #mainloop is our ending line for any tkinter window, without it the application will not run

# NOW Time to do some basic config with our window. Like you can give Title and, dimensions to it,
#  can make it resizable upto some limit or even fix the size 

main=Tk()
main.title("resizing window")
# .geometry("widthxheight")
main.geometry("500x400")   #the window will be having this size when program starts
main.minsize(300, 200)    #the lower you can resize it
main.maxsize(600, 500)    #the maximum size upto which you can stretch it
main.mainloop()



# you can even fix the position at which the window should pop at start
# for this first get some knowledge of dimensions of your desktop. 
# the uppermost left position acts like origin where x=y=0
# like we move downwards , y increases and when we move towards right , x increases
# the last point or point having maximum values is at bottom right of yor desktop

# Now for the above said property to get , copy the following line of code and replace it with main.geometry("500x400")
# ----- main.geometry("500x400+100+200") ------   100 is value for x,200 for y


# ------------------------------------------------------------------------------------
# Challenge: make some more changes with dimensions,study graph, and check whether even after giving maximum dimension
#  of your screen, the tkinter window would cover all the space or not
# ------------------------------------------------------------------------------------