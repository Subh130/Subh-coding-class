from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#setting up main window
window = Tk()
window.title("denomination counter")
window.config(bg = "aqua")
window.geometry("600x400")

#adding images and labels in the main window
upload = Image.open("app-image.jpeg")

upload =  upload.resize((300, 300)) #resize the image using resize method
image = ImageTk.PhotoImage(upload)
label = Label(window, image=image, bg= "light blue")
label.place(x=120, y=20)

label1 = Label(window,
               text= "hello, Welcome to denomination counter application.",
               bg= "aqua")

label1.place(relx= 0.5, y= 340, anchor= CENTER)

#function to display a message box and proceed if OK is clicked
def msg():
    MsgBox= messagebox.showinfo( 
        "alert", "Do you want to calculate the demolition count?")
    if MsgBox == "ok":
        topwin()

#adding button to the main window
button1 = Button(window,
                text="Lets get started!",
                command = msg,
                bg = "green",
                fg = "white")
button1.place(x=260, y=360)

#function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Demoninations den_counter")
    top.config(bg="light yellow")
    top.geometry("600x350+50+50")

    label= Label(top, text="Enter total amount", bg="light yellow")
    entry = Entry(top)
    lb1 = Label(top, text="Here are no of notes for each demoninations", bg="light yellow")

    l1 = Label(top, text="2000", bg="light yellow")
    l2 = Label(top, text="1000", bg="light yellow")
    l3 = Label(top, text="500", bg="light yellow")
    l4 = Label(top, text="100", bg="light yellow")

    t1= Entry(top)
    t2= Entry(top)
    t3= Entry(top)
    t4= Entry(top)

    def den_counter():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000

            note1000 = amount // 1000
            amount %= 1000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100
            amount %= 100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note1000))
            t3.insert(END, str(note500))
            t4.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn= Button(top, text="calculate", command=den_counter, bg="lime", fg="black")

    #centering widgets in top window
    label.place(x=250, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lb1.place(x=140, y= 170)

    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    l4.place(x=180,y=290)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    t4.place(x=270, y=290)

    top.mainloop()

window.mainloop()