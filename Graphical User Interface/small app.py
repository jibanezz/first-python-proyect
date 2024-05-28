import tkinter as tk
from tkinter import messagebox

# Initialize the list of registered users
registered_users = []

def calculate_bill():
    hours = int(entry_hours.get())
    name = entry_name.get()

    if hours > 72 and name not in registered_users:
        messagebox.showinfo("Error", "You have been parked for more than 72 hours. Your car is now in the police station.")
        return

    rate = 0
    if hours <= 5:
        rate = 1
    elif 5 < hours <= 10:
        rate = 0.8
    elif 10 < hours <= 24:
        rate = 0.7
    else:
        rate = 0.6

    total_bill = hours * rate

    # Apply a 40 percent discount for registered users
    if name in registered_users:
        total_bill *= 0.6

    if name in registered_users:
        result_label.config(text=f"Hi {name}, your bill is ${total_bill:.2f} with a 40% discount, now ${total_bill * 0.6:.2f}")
    else:
        result_label.config(text=f"Hi {name}, your total bill is ${total_bill:.2f}")

def on_continue():
    regis = regis_entry.get()
    if regis != '':
        registered_users.append(regis)
        messagebox.showinfo("Registration", f"{regis} is now registered")
    entry_hours.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("Car Parking Ticket System")

# Create and place widgets
label_hours = tk.Label(window, text="How many hours have you been parked?")
label_hours.pack()

entry_hours = tk.Entry(window)
entry_hours.pack()

label_name = tk.Label(window, text="Please enter your name:")
label_name.pack()

entry_name = tk.Entry(window)
entry_name.pack()

calculate_button = tk.Button(window, text="Calculate Bill", command=calculate_bill)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

continue_button = tk.Button(window, text="Continue", command=on_continue)
continue_button.pack()

regis_label = tk.Label(window, text="Please enter name to register (leave empty to skip):")
regis_label.pack()

regis_entry = tk.Entry(window)
regis_entry.pack()

# Start the GUI event loop
window.mainloop()
