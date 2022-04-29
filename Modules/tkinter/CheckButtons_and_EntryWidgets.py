from tkinter import *

root = Tk()
root.geometry("644x444")
root.title("Check Buttons and Entry Widgets")


gender_list = ["", "Male", "Female", "Others"]
payment_mode_list = ["", "Cash", "Net-Banking"]


def display_data():
    print("Name :", name.get())
    print("Gender :", gender_list[gender.get()])
    print("Phone No. :", phone.get())
    print("Payment Mode :", payment_mode_list[payment_mode.get()])


# Adding labels for the entries
Label(text="Welcome !!!", font=("Times New Roman", 15, "bold")).grid(
    row=0, column=3, pady=5, padx=10)  # one liner
Label(text="Name", font=("Times New Roman", 10, "bold")).grid(
    row=1, column=0, pady=5)  # one liner
Label(text="Gender", font=("Times New Roman", 10, "bold")).grid(
    row=2, column=0, pady=5)  # one liner
Label(text="Phone", font=("Times New Roman", 10, "bold")).grid(
    row=3, column=0, pady=5)  # one liner
Label(text="Payment Mode", font=("Times New Roman", 10, "bold")).grid(
    row=4, column=0, pady=5)  # one line

# Adding Entries
name = StringVar()
gender = IntVar()  # to make a checkbox
phone = StringVar()
payment_mode = IntVar()  # to make a checkbox

Entry(root, textvariable=name).grid(row=1, column=1, pady=5)
Entry(root, textvariable=phone).grid(row=3, column=1, pady=5)

# Adds just one check box (0 or 1)
# Checkbutton(text = "Male", variable = gender).grid(row = 2, column = 1)

# Adding multiple checks (to choose "only" one) using CheckButtons
Checkbutton(text = "Male", variable = gender, onvalue = 1).grid(row = 2, column = 1)
Checkbutton(text = "Female", variable = gender, onvalue = 2).grid(row = 2, column = 2)
Checkbutton(text = "Others", variable = gender, onvalue = 3).grid(row = 2, column = 3)

Checkbutton(text = "Cash", variable = payment_mode, onvalue = 1).grid(row = 4, column = 1)
Checkbutton(text = "Net-Banking", variable = payment_mode, onvalue = 2).grid(row = 4, column = 2)

# Adding multiple checks (to choose "only" one) using "RadioButtons"
# gender
# Radiobutton(root, text="Male", variable=gender, value=1).grid(row=2, column=1)
# Radiobutton(root, text="Female", variable=gender,
#             value=2).grid(row=2, column=2)
# Radiobutton(root, text="Others", variable=gender,
#             value=3).grid(row=2, column=3)

# # payment mode
# Radiobutton(root, text="Cash", variable=payment_mode,
#             value=1).grid(row=4, column=1)
# Radiobutton(root, text="Net Banking", variable=payment_mode,
#             value=2).grid(row=4, column=2)

# Submit button
Button(root, text="Submit", command=display_data).grid(row=5, column=3)

root.mainloop()
