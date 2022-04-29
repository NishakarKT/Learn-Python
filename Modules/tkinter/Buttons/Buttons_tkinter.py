from tkinter import *

root = Tk()
root.geometry("644x444")
root.title("Buttons using tkinter")

f1 = Frame(root, bg = 'green', borderwidth = 15, relief = SUNKEN)
f1.pack(side = TOP, fill = X)

b1 = Button(f1, text = "PLAY", fg = "yellow", bg = "blue", font = "bold", borderwidth = 10, relief = RAISED)
b1.pack(side = BOTTOM, anchor = 'ne')
b2 = Button(f1, text = "STOP", fg = "yellow", bg = "blue", font = "bold", borderwidth = 10, relief = RAISED)
b2.pack(side = BOTTOM, anchor = 'ne')
b3 = Button(f1, text = "ADD", fg = "yellow", bg = "blue", font = "bold", borderwidth = 10, relief = RAISED)
b3.pack(side = BOTTOM, anchor = 'ne')
b4 = Button(f1, text = "REMOVE", fg = "yellow", bg = "blue", font = "bold", borderwidth = 10, relief = RAISED)
b4.pack(side = BOTTOM, anchor = 'ne')

label = Label(f1, text = 'Buttons', bg = 'yellow', fg = "black", font = ("Times New Roman", 20, "bold"))
label.pack(fill = X)

root.mainloop()