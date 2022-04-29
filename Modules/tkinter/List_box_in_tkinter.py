from tkinter import *

def add():
    global i
    i += 1
    list_box.insert(ACTIVE, f"{i} Hello World !!!") # inserts the element "above" the "mouse pointer selected" element

i = 0
root = Tk()
root.title("List Box in Python")
root.geometry("644x444")

list_box = Listbox(root)
list_box.pack()

list_box.insert(END, "First item of our List Box") # adds at the end of the last item

Button(root, text = "Add Item",command = add).pack()
root.mainloop()