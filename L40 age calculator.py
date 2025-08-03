from tkinter import *
from datetime import date

window = Tk()
window.title("Age Calculator")
window.geometry("400x400")

def age():
    try:
        # Get today's date
        today = date.today()

        # Extract and convert input values
        name = name_entry.get()
        birth_year = int(year_entry.get())
        birth_month = int(month_entry.get())
        birth_day = int(day_entry.get())

        # Calculate age
        birth_date = date(birth_year, birth_month, birth_day)
        age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        age_months = (today.month - birth_date.month) % 12
        age_days = (today - birth_date).days

        # Display results
        tsk.delete("1.0", END)  # Clear previous output
        tsk.insert(END, f"Hey {name}!\n")
        tsk.insert(END, f"Years: {age_years}\n")
        tsk.insert(END, f"Months (approx): {age_months}\n")
        tsk.insert(END, f"Total Days: {age_days}")
    except Exception as e:
        tsk.delete("1.0", END)
        tsk.insert(END, f"Error: {e}")

# UI layout
new_frame = Frame(master=window, height=250, width=360, bg="#00ffff")

lb1 = Label(new_frame, text="Input name", fg="black", bg="black", height=1, width=15)
name_entry = Entry()

lb2 = Label(new_frame, text="Input birth year", fg="white", bg="black", height=1, width=15)
year_entry = Entry()

lb3 = Label(new_frame, text="Input birth month", fg="white", bg="black", height=1, width=15)
month_entry = Entry()

lb4 = Label(new_frame, text="Input birth day", fg="white", bg="black", height=1, width=15)
day_entry = Entry()

tsk = Text(bg="white", fg="black", height=5, width=45)

btn = Button(text="Calculate Age", command=age, bg="red", fg="yellow")

# Placing widgets
new_frame.place(x=20, y=0)

lb1.place(x=20, y=20)
name_entry.place(x=150, y=20)

lb2.place(x=20, y=60)
year_entry.place(x=150, y=60)

lb3.place(x=20, y=100)
month_entry.place(x=150, y=100)

lb4.place(x=20, y=140)
day_entry.place(x=150, y=140)

btn.place(x=130, y=270)
tsk.place(x=20, y=310)

window.mainloop()
