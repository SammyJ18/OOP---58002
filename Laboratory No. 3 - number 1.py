from tkinter import *

class MyWindow:
    def __init__(self, window):
        self.label_title = Label(window, text="Laboratory Activity 5")
        self.label_title.place(x=200, y=40)

        self.label_submitted = Label(window, text="Submitted to Mam Sayo")
        self.label_submitted.place(x=188, y=70)

window = Tk()
MyWindow(window)
window.geometry("500x300+10+10")
window.title("Label")
window.mainloop()
