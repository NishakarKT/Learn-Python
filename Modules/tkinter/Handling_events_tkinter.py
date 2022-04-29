from tkinter import *

def func1(event):
    print(f"Good Morning\nYou clicked at ({event.x}, {event.y})")
root = Tk()

root.title("Event Handling")
root.geometry("644x444")

sample_button = Button(root, text = "Click Me, Please", bg = "yellow", fg = "black", relief = RAISED)
sample_button.grid()
sample_button.bind('<Button-1>', func1)
sample_button.bind('<Double-1>', quit)
root.mainloop()