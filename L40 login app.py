from tkinter import *

#create window
window = Tk()
window.title("login app")
window.geometry("400x400")

def display():
    name = name_entry.get()
    greet = "Hey " + name
    message = "\ncongratulations for your new account"
    res.insert(END,greet)
    res.insert(END, message)

#create widgets
new_frame = Frame(master=window, height= 200, width=360, bg = "#00ffff")

LbL1 = Label(new_frame, text="Full name", bg="green", fg = "white", width=12)
LbL2 = Label(new_frame, text="Email Id", bg="green", fg = "white", width=12)
LbL3 = Label(new_frame, text="Enter passoword", bg="green", fg = "white", width=12)

name_entry = Entry(new_frame)
email_entry = Entry(new_frame)
pass_entry = Entry(new_frame, show="*")

res = Text(bg="white", fg="black")

btn = Button(text="create acoount", command=display, bg = "red", fg = "yellow")

#arrange all widgets
new_frame.place(x = 20, y = 0)

LbL1.place(x=20, y=20)
name_entry.place(x = 150, y = 20)

LbL2.place(x=20, y=80)
email_entry.place(x = 150, y = 80)

LbL3.place(x=20, y=140)
pass_entry.place(x = 150, y = 140)

btn.place(x = 130, y= 210)

res.place(y = 250)

window.mainloop()