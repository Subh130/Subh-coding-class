from tkinter import *
from tkinter import messagebox

#setup the window
window = Tk()
window.geometry("250x250")
window.title("Virus detected")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found")

#add widgets
btn = Button(window, text="Scan for virus", command=msg)
btn.place(x=75, y=80)

window.mainloop()