from tkinter import *

class MyWindow:
    def __init__(self, window):
        self.label_title = Label(window, text="Charles Babbage", bg="#00FFFF", font=("Verdana", 20))
        self.label_title.place(x=100, y=100)

    def clear_text(self, event):
        self.in1.delete(0, "end")

window = Tk()
MyWindow(window)
window.geometry("500x300+10+10")
window.mainloop()
