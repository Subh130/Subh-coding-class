from tkinter import *

window = Tk()
window.geometry("600x500")
window.title("product")

def product():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    product = num1*num2
    message = f"The product is {product}\n"
    text_box.insert(END, message)

def sum():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    sum = num1+num2
    message = f"The sum is {sum}\n"
    text_box.insert(END, message)

def substraction():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    diffrence = num1-num2
    message = f"The diffrence is {diffrence}\n"
    text_box.insert(END, message)

def division():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    division = num1/num2
    message = f"{num1}/{num2} = {division}\n"
    text_box.insert(END, message)

lb1 = Label(text="input first number", fg="white", bg="black", height=1, width=300)
num1_entry = Entry()
lb2 = Label(text="input second number", fg="white", bg="black", height=1, width=300)
num2_entry = Entry()

text_box = Text(height=4)

btn1 = Button(text="Product",command=product,height=1, bg="red", fg="white" )
btn2 = Button(text="Sum",command=sum, height=1, bg="blue", fg="white" )
btn3 = Button(text="substraction",command=substraction, height=1, bg="blue", fg="white" )
btn4 = Button(text="division",command=division, height=1, bg="blue", fg="white" )


lb1.pack()
num1_entry.pack()
lb2.pack()
num2_entry.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
text_box.pack()

window.mainloop()