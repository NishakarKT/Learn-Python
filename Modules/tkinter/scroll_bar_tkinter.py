from tkinter import *

root = Tk()
root.title("ScroLL Bar")
root.geometry("644x444")

# STEPS
# (1) widget(vscrollcommand = scrollbar.set)
# (2) scrollbar.config(command = widget.yview)

# creating a scroll bar widget
# scroll_bar = Scrollbar(root)
# scroll_bar.pack(side=RIGHT, fill=Y)

# # STEP 1
# list_box = Listbox(root, yscrollcommand=scroll_bar.set)
# for i in range(1, 51):
#     list_box.insert(END, f"Item no. {i}")
# list_box.pack(fill=BOTH)

# # Step 2
# scroll_bar.config(command=list_box.yview)
# root.mainloop()

########################################################################
# Scroll bar linking to text.. like in Notepad

scroll_bar = Scrollbar(root)
scroll_bar.pack(side = RIGHT, fill = Y)

# Creating a text variable
text = Text(root, yscrollcommand = scroll_bar.set)
text.pack(fill = BOTH)

scroll_bar.config(command = text.yview)
root.mainloop()
