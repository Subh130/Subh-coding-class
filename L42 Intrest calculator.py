import tkinter as tk
from tkinter import messagebox

# Function to calculate interest
def calculate_interest():
    try:
        p = float(principle_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        simple_interest = (p * t * r) / 100
        compound_interest = p * ((1 + r / 100) ** t - 1)

        si_value_label.config(text=f"{simple_interest:.2f}")
        ci_value_label.config(text=f"{compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numeric values.")
        
root = tk.Tk()
root.geometry("400x400")
root.title("Age Calculator App")

bg_color = "#f0f8ff"  
label_color = "#4682b4"  
entry_bg = "#ffffff" 
button_bg = "#32cd32"

root.configure(bg=bg_color)

tk.Label(root, text="Principle:", bg=bg_color, fg=label_color, font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
principle_entry = tk.Entry(root, bg=entry_bg, width=20)
principle_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Time (years):", bg=bg_color, fg=label_color, font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
time_entry = tk.Entry(root, bg=entry_bg, width=20)
time_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Rate of Interest (%):", bg=bg_color, fg=label_color, font=("Arial", 12, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
rate_entry = tk.Entry(root, bg=entry_bg, width=20)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Calculate", bg=button_bg, fg="white", font=("Arial", 12, "bold"), command=calculate_interest).grid(row=3, column=0, columnspan=2, pady=20)

tk.Label(root, text="Simple Interest:", bg=bg_color, fg=label_color, font=("Arial", 12, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
si_value_label = tk.Label(root, text="0.00", bg=bg_color, fg="black", font=("Arial", 12))
si_value_label.grid(row=4, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="Compound Interest:", bg=bg_color, fg=label_color, font=("Arial", 12, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
ci_value_label = tk.Label(root, text="0.00", bg=bg_color, fg="black", font=("Arial", 12))
ci_value_label.grid(row=5, column=1, padx=10, pady=10, sticky="w")

root.mainloop()
