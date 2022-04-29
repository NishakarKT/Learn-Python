from tkinter import *

root = Tk()
root.title("FRAMES")
root.geometry("644x400")

frame1 = Frame(root, bg = "yellow", borderwidth = 20, relief = SUNKEN)
frame1.pack(side = LEFT, fill=Y, pady = 25)

frame2 = Frame(root, bg = "yellow", borderwidth = 20, relief=SUNKEN)
frame2.pack(side = TOP, fill = X)

label = Label(frame1, text = "Frame1")
label.pack()
label = Label(frame2, text="Frame2")
label.pack()

root.mainloop()