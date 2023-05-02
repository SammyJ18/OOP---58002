import tkinter as tk

window = tk.Tk()
window.geometry("500x300+10+10")
window.title("a, a^2, a^3")

# create a table with headings
tk.Label(window, text="a").grid(row=0, column=0)
tk.Label(window, text="a^2").grid(row=0, column=1)
tk.Label(window, text="a^3").grid(row=0, column=2)

# populate the table with values
for i in range(1, 5):
    tk.Label(window, text=str(i)).grid(row=i, column=0)
    tk.Label(window, text=str(i*i)).grid(row=i, column=1)
    tk.Label(window, text=str(i*i*i)).grid(row=i, column=2)

window.mainloop()
