from tkinter import *

class GUI (Tk): # Inheriting GUI class (my class) form Tk() class ...
    def __init__(self):
        super().__init__()
        self.geometry("644x444")
    
    def status(self):
        self.status_var = StringVar()
        self.status_var.set("Ready")
        self.s_bar = Label(self, textvar = self.status_var, anchor = 'w', relief = SUNKEN)
        self.s_bar.pack(side = BOTTOM, fill = X)

    def create_button(self, button_text):
        self.button = Button(self, text = button_text)
        self.button.pack()

if __name__ == "__main__":
    window = GUI()
    window.status()
    window.create_button("Play")
    window.mainloop()
