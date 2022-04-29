from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("644x444")
photo = Image.open("Images in tkinter\\Haunter2.jpg")
PHOTO = ImageTk.PhotoImage(photo)

label = Label(image = PHOTO)
label.pack()
root.mainloop()