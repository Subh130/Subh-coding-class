from tkinter import *

#create window
window = Tk()
window.title("Event Handler")
window.geometry("250x250")

#event handler for keypress
def handle_keypress(event):
    print(event.char)

# bind key press event to handle_keypress()
window.bind("<Key>", handle_keypress)

#event handler for button click
def handle_click(event):
    print("The button was clicked")

#add widgets
button = Button(text="Click me!")
button.pack()

#bind click event to handle_click
window.bind("<Button-1>", handle_click)

window.mainloop()