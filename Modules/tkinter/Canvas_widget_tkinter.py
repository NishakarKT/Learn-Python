from tkinter import *

root = Tk()
root.title("Canvas")

# Canvas
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")

canvas_widget = Canvas(root, width=canvas_width,
                       height=canvas_height, bg="yellow")
canvas_widget.pack()

# create a line
canvas_widget.create_line(10, 10, 200, 200, fill="red") # line between ((0,0) to (200,200))
canvas_widget.create_line(200, 10, 10, 200, fill="red") # line between ((0,0) to (200,200))

# create a rectanglie
# reactangle with ... (coordinates of top left, coordinates of bottom right)
canvas_widget.create_rectangle(300, 10, 500,500, fill = "green") # "fill" fills the interior with the mentioned colour

# creates text
canvas_widget.create_text(50, 250, text = "Hello World !!!", fill = "blue") # (50, 250) is for the centre of the text

# create oval
canvas_widget.create_oval(50, 300, 100, 600, fill = "red") # we give coordinates of a rectangle. Max size oval inside is going to get created

root.mainloop()
