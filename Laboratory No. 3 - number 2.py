from tkinter import *

class Name:
    def __init__(self, win):
        self.in1 = Entry(win, borderwidth=3, width=10)
        self.in1.insert(0, "This is where I type my text")
        self.in1.bind("<FocusIn>", self.clear_text)
        self.in1.place(x=150, y=50, width=155, height=50)

    def clear_text(self, event):
        self.in1.delete(0, "end")

window = Tk()
winn = Name(window)
window.geometry("500x150+10+10")
window.title("Text Field")
window.mainloop()
