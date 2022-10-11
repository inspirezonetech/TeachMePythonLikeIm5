# You all would be wondering what are uses of GUI and how to achieve its functionality
# now , to answer this , there is tutorial_2 where you would learn about widgets, what are they 
# and we will discuss some of them

# WIDGETS: Tkinter provides various controls, such as buttons, 
# labels and text boxes used in a GUI application. These controls are commonly called widgets.

# There are many attributes associated with each widgets like dimensions, colors, fonts, borders, relief styles
# , text-alignment, and sometimes placeholder

# first widget to be started is with : FRAME
# frame is like a container which contains other widgets in it
# by which we can divide our window in parts and make changes to each one independently
# for simple learning first move to code, analyze how it works then you will get clear idea
from tkinter import*
main=Tk()
main.geometry("400x400")
#frame_widget = Frame(parent_window, attributes...)
frame_widget = Frame(main)  #read about its syntax also 
# now you wouldn't be noticing any change as whev we do not specify dimension of frame widget
#  it covers whole window now we would learn about its attriutes, like dimensions
# , border which would help you separate frame from parent window

# comment above code line
frame_widget = Frame(main)
frame_widget.pack(side=RIGHT)  # this line is one of the important as many coders forget about it, thus resulting in no output
# we need to give each widget some packing status or we need to tell them their position with respect to parent window

frame_widget_2 = Frame(main)
frame_widget_2.pack(side="left")

btn1 = Button(frame_widget, text="Submit", fg="red",bg="yellow", height=4,width=5)
btn1.pack()  
#here you can see button is being located at right side of parent window, even it is not having direct connection with it
# that's possible as it is configured with frame widget which contains it
btn2 = Button(frame_widget_2, text="Collect", fg="blue",bg="white", height=4,width=5)
btn2.pack() 

main.mainloop()