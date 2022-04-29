from tkinter import *


def getting_dollars():
    print(f"Transacted Amount: {my_slider1.get()}")


root = Tk()
root.title("sliders in tkinter")
root.geometry("644x444")

# Vertical Slider
my_slider1 = Scale(root, from_=100, to=0)
my_slider1.pack()
my_slider1.set(50) # Setting initial value of the slider
Label(root, text="How many dollars do you want ?").pack()
Button(root, text="Get Dollars", command=getting_dollars).pack()

# Horizontal Slider
my_slider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval = 25)
my_slider2.pack()


root.mainloop()
