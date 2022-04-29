from tkinter import *

root = Tk()

# right now .jpg format is not supported
photo = PhotoImage(file="Images in tkinter\\Landscape.png")
label = Label(image=photo)
label.pack()
root.mainloop()
