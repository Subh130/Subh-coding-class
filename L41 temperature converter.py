import tkinter as tk

#setup the window
window = tk.Tk()
window.title("Temperature converter")
window.geometry("250x75")
window.resizable(width = False, height = False)

def farenheit_to_celcius():
    farenheit = ent_temperature.get()
    celsius = (5/9)*(float(farenheit)-32)
    lb1_result["text"]= f"{round(celsius-2)} \N{DEGREE CELSIUS}"

#create widget
frm_entry = tk.Frame(master = window)
ent_temperature = tk.Entry(master = frm_entry, width = 10)
lb1_temp = tk.Label(master = frm_entry, text= "\N{DEGREE FAHRENHEIT}")

btn_convert = tk.Button(master = window, text = "-->", command = farenheit_to_celcius)
lb1_result = tk.Label(master = window, text = "\N{DEGREE CELSIUS}")

#arrange the widgets
frm_entry.grid(row = 0, column = 0 , padx = 10)
ent_temperature.grid(row=0, column = 0, sticky = "e")
lb1_temp.grid(row = 0 , column = 1, sticky = "w")
btn_convert.grid(row = 0, column = 1, pady =0 )
lb1_result.grid(row = 0, column = 2, padx =10)

window.mainloop()