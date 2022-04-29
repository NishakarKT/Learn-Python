from tkinter import *  # it means to import "everything"

def check():
    if(username_value.get() == password_value.get()):
        print("Access Granted !!!")
    else:
        print("Accesss Denied ...")
        
root = Tk()
root.geometry("644x444")
root.title("GRIDS")

# just like .pack(), .grid() is another way of packing in grid style
username = Label(text="Username")
username.grid()
password = Label(text="Password")
password.grid()

# Varibale classes in tkinter
# 1) BooleanVar
# 2) DoubleVar
# 3) StringVar
# 4) IntVar

username_value = StringVar()
password_value = StringVar()

# creating 2 entries
user_entry = Entry(root, textvariable = username_value)
user_entry.grid(row = 0, column = 1)
pass_entry = Entry(root, textvariable = password_value)
pass_entry.grid(row = 1, column = 1)

# button
b1 = Button(root, text="Login", bg = "yellow", fg = "black", borderwidth = 5, command = check)
b1.grid()


root.mainloop()