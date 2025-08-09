import tkinter as tk

def convert_to_cm():
    try:
        inches = float(entry_inch.get())
        cm = inches * 2.54
        result_label.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

root = tk.Tk()
root.title("Inches to Centimeters Converter")

label_inch = tk.Label(root, text="Enter length in inches:")
label_inch.pack(pady=5)

entry_inch = tk.Entry(root)
entry_inch.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
