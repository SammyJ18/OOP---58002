from tkinter import *
class MyWindow:
    def __init__(self,win):
        self.lbl1=Label(win,text="<--Click to Change the color of the button", borderwidth=1,relief='raised')
        self.lbl1.place(x=125,y=150)
        self.btn1 = Button(win, text="Color",bg='Blue',fg='Red',command = self.Change)
        self.btn1.place(x=75,y=150)

    def Change(self):
        self.btn1.configure(bg='Yellow')

window = Tk()
mywin = MyWindow(window)
window.geometry("400x200+10+10")
window.title("Button")
window.mainloop()