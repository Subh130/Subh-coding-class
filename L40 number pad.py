from tkinter import *

window  =  Tk()
window.title = ("Number pad")
window.geometry = ("250x300")

#create the number grid
nums = [[9,8,7], [6,5,4], [3,2,1], ["#",0 , "*"] ]

#configure rows and columns to resize window
for i in range(4):
    window.columnconfigure(i, weight = 1, minsize=75 )
    window.rowconfigure(i, weight = 1, minsize=50)


for i in range (4):
    for j in range(3):
        new_frame = Frame(
            master=window,
            relief=SUNKEN,
            borderwidth=1,
            bg="red"
        )

        new_frame.grid(row=i, column=j, sticky="nsew")

        label2 = Label(master=new_frame, text=nums[i][j], bg = "lime", font=("Arial", 18))
        label2.pack(expand=True, fill="both", padx=5, pady=5)

window.mainloop()