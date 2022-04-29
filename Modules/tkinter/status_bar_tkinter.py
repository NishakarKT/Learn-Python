from tkinter import *

def update():
    status_var.set("Busy..")
    s_bar.update() # you have to update or it wont show up
    import time
    time.sleep(2)
    status_var.set("Free..")
root = Tk()
root.title("Status Bar")
root.geometry("644x444")

status_var = StringVar()
status_var.set("Ready")

s_bar = Label(root, textvariable = status_var, relief = SUNKEN, anchor = 'w')
s_bar.pack(side = BOTTOM, fill = X, padx = 5, pady = 5)

Button(root, text = "Update", command = update).pack()
root.mainloop()