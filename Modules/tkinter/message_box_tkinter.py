from tkinter import *
from tkinter import messagebox as tmsg

def save():
    value = tmsg.askquestion("Save", "Would you like to save your existing file ?")
    if(value == 'yes'):
        while(True):
            if(tmsg.askretrycancel("Save", "A problem occured ...") == False):
                break

def func1():
    print("Files opened...")

def help():
    return tmsg.showinfo("Help", "I will help you ...")


def rate():
    # returns yes or no <-- tmsg.askquestion("Rate Us", "Did you have a wonderful experience ???")
    value = tmsg.askquestion("Rate Us", "Did you have a wonderful experience ???")

    if(value == 'yes'):
        tmsg.showinfo("Rate Us", "Thanks...\nPlease rate us on Store...")
    else:
        tmsg.showinfo("Rate Us", "Tell us how we may improve...\nYour feedback would be appreciated...")


root = Tk()
root.title("Menus and Sub_Menus")
root.geometry("644x444")
my_menu_2 = Menu(root)

m1 = Menu(my_menu_2, tearoff=0)
m1.add_command(label="Save", command=save)
m1.add_command(label="Save As", command=func1)
m1.add_command(label="Print", command=func1)
root.config(menu=my_menu_2)
my_menu_2.add_cascade(label="FILE", menu=m1)

# m2 for other menu
m2 = Menu(my_menu_2, tearoff=0)
m2.add_command(label="Save", command=func1)
m2.add_separator()
m2.add_command(label="Save As", command=func1)
m2.add_separator()
m2.add_command(label="Print", command=func1)
m2.add_separator()
root.config(menu=my_menu_2)
my_menu_2.add_cascade(label="VIEW", menu=m2)

# m3 the third smenu to show the dialog box
m3 = Menu(my_menu_2, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate us", command=rate)
my_menu_2.add_cascade(label="HELP", menu=m3)
root.config(menu=my_menu_2)

root.mainloop()
