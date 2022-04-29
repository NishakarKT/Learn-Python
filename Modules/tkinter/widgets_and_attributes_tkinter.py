from tkinter import *

root = Tk()

# setting original size
root.geometry("644x434")  # (widthxheight)
# setting MIN size of the GUI window
root.minsize(200, 100)  # (width, height)
# setting MAX size of the GUI window
root.maxsize(800, 800)  # (width, height)

label = Label(text="Hello World !!!")
label.pack()  # we have to pack a label in order to see it function

# Creating a Label (Widget which doesn't interact with the User, unlike Buttons)

root.mainloop()
