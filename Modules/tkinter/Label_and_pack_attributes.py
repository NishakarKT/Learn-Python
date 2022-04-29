from tkinter import *

root = Tk()

root.title("Label Atributes !!!")

# Label Attributes
# 1) text --> adds text
# 2) bd --> background
# 3) fg --> foreground
# 4) font --> sets the font ... ""font=(FontName, FontSize, FontType)"" (FontType = "bold" etc.)
# 5) padx --> x padding implies extending of the background in X direction
# 6) pady --> y padding implies extending of the background in Y direction
# 7) relief --> border styling ==> SUNKEN, RAISED, GROOVE, RIDGE

label = Label(text="Hello World !!!", bg="yellow", fg="black", padx=120, pady=120, font=(
    "Times New Roman", 30, "bold"), borderwidth=3, relief=RAISED)

# Pack Attributes
# 1) anchor = nw
# 2) side = TOP, BOTOM, LEFT, RIGHT (by default TOP)
# 3) fill
# 4) padx
# 5) pady

label.pack(fill = X) # fills screen in the X direction

# label.pack(anchor="ne")  # display runs towards north-east
# label.pack(side=BOTTOM, anchor="ne")  # display runs towards south-east
# label.pack(side=BOTTOM, anchor="nw")  # display runs towards south-east
# label.pack(side=BOTTOM, anchor="se")  # display runs towards south-east
# label.pack(side=BOTTOM, anchor="sw")  # display runs towards south-east
# label.pack(side=LEFT)  # display runs towards south-east
# label.pack(side=RIGHT)  # display runs towards south-east

root.mainloop()
