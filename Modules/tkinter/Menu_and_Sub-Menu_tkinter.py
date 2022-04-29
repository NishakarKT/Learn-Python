from tkinter import *

def func1():
    print("Files opened...")

root = Tk()
root.title("Menus and Sub_Menus")
root.geometry("644x444")

# "Menu" widget
# my_menu_1 = Menu(root)
# my_menu_1.add_command(label = "File", command = func1)
# my_menu_1.add_command(label = "Exit", command = quit)
# root.config(menu=my_menu_1)

# Sub_Menus with "tearoff"
# my_menu_2 = Menu(root)

# m1 = Menu(my_menu_2)
# m1.add_command(label = "Save", command = func1)
# m1.add_command(label = "Save As", command = func1)
# m1.add_command(label = "Print", command = func1)
# root.config(menu = my_menu_2)
# my_menu_2.add_cascade(label = "FILE", menu = m1)

# Sub-Menus without "tearoff"
my_menu_2 = Menu(root)

m1 = Menu(my_menu_2, tearoff = 0)
m1.add_command(label = "Save", command = func1)
m1.add_separator()
m1.add_command(label = "Save As", command = func1)
m1.add_separator()
m1.add_command(label = "Print", command = func1)
m1.add_separator()
root.config(menu = my_menu_2)
my_menu_2.add_cascade(label = "FILE", menu = m1)

# m2 for other menu
m2 = Menu(my_menu_2, tearoff = 0)
m2.add_command(label = "Save", command = func1)
m2.add_separator()
m2.add_command(label = "Save As", command = func1)
m2.add_separator()
m2.add_command(label = "Print", command = func1)
m2.add_separator()
root.config(menu = my_menu_2)
my_menu_2.add_cascade(label = "VIEW", menu = m1)

root.mainloop()