from tkinter import *

root = Tk()
root.geometry("644x444")
root.title("Buttons 2")


def text_print():
    user = input("Enter text : ")
    print(user)


f1 = Frame(root, bg="yellow", borderwidth=15, relief=SUNKEN)
f1.pack(fill=X)

f2 = Frame(root, bg="orange", borderwidth=15, relief=SUNKEN)
f2.pack(side=BOTTOM, fill=X)

b1 = Button(f2, text="Text", bg="red", fg="yellow", font=(
    "Times New Roman", 15, "bold"), relief=SUNKEN, borderwidth=15, command=text_print)
b1.pack()

label = Label(f1, text="Frame 1", font=("Times New Roman", 30, "bold"),
              bg="green", fg="black", borderwidth=10, relief=RAISED)
label.pack(fill=X)
label = Label(f2, text="Frame 2", font=("Times New Roman", 30, "bold"),
              bg="orange", fg="yellow", borderwidth=10, relief=RAISED)
label.pack(fill=X)

root.mainloop()
