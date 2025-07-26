from tkinter import *
from datetime import date

#create a window
window = Tk()
window.title("Getting started with widgets")
window.geometry("600x500")

def display():#function to display a message
    name = name_entry.get()

    #declaring a global variable
    #to make is accessible throught the program
    global message
    message = "Welcome to application! \nToday's date is: "
    greet = "Hello "+name+"\n"

    #display details in a text box
    #specify where to add  the details isnide the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

#create widgets
lb1 = Label(text = "Hey there!", fg = "white", bg = "#072F5F", height = 1, width = 300)

name_lb1 = Label(text = "Enter your full name", bg = "blue", fg = "white")
name_entry = Entry()#text input

text_box = Text(height=3)

btn = Button(text = "Display message", command=display, height = 1, bg = "red", fg = "white")


#Attaching all the widgets in the window
lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()