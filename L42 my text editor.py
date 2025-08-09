from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

#setup root window
window = Tk()
window.title("My Text editor")
window.geometry("600x500") # widtn = 600, height = 500
window.rowconfigure(0, minsize=800, weight = 1)
window.columnconfigure(1, minsize= 800, weight= 1)

#a function to open a file
def open_file():
    #open file
    filepath = askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if not filepath:
        return
    
    txt_edit.delete(1.0, END)

    #if a file is opened then display the contents of the file
    with open(filepath, "r") as input_file:
        text = input_file.read() #read contents of the input file

        txt_edit.insert(END, text)# insert contents of the file in the editor bos

        input_file.close()
    window.title(f"My Text editor - {filepath}")

#function to save a file
def save_file():
    #save the current file as a new file
    filepath = asksaveasfilename( 
                                defaultextension="txt",
                                filetypes=[("Text files","*.txt"), ("All files", "*.*")]
                                )
    if not filepath:
        return
    
    with open(filepath,"w") as output_file:
        text = txt_edit.get(1.0, END)#read the edited content
        output_file.write(text) #update in the file output

    window.title(f"My text editor - {filepath}")

#create widgets
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open= Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text = "Save as...", command=save_file)

#arrange the widgets
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row = 1, column=0, sticky ="ew", padx = 5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()