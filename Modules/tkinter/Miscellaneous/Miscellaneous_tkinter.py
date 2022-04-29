from tkinter import *

root = Tk()
root.title("Miscellaneous")
root.geometry("644x444")

# setting icons
root.wm_iconbitmap("fb.ico")

# Dark Theme ...
root.configure(background = "black")

# close window
Button(text = "close", command = root.destroy).pack()
root.mainloop()