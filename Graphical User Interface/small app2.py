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

# Configure window size and position
window.geometry("400x300")
window.resizable(False, False)

# Set a background color
window.configure(bg="#f0f0f0")

# Create and place widgets with styling
header_label = tk.Label(window, text="Car Parking Ticket System", font=("Helvetica", 16), bg="#f0f0f0")
header_label.pack(pady=10)

label_hours = tk.Label(window, text="How many hours have you been parked?", font=("Helvetica", 12), bg="#f0f0f0")
label_hours.pack()

entry_hours = tk.Entry(window, font=("Helvetica", 12))
entry_hours.pack()

label_name = tk.Label(window, text="Please enter your name:", font=("Helvetica", 12), bg="#f0f0f0")
label_name.pack()

entry_name = tk.Entry(window, font=("Helvetica", 12))
entry_name.pack()

calculate_button = tk.Button(window, text="Calculate Bill", font=("Helvetica", 12), command=calculate_bill, bg="#4caf50", fg="white")
calculate_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#f0f0f0")
result_label.pack()

continue_button = tk.Button(window, text="Continue", font=("Helvetica", 12), command=on_continue, bg="#2196f3", fg="white")
continue_button.pack(pady=10)

regis_label = tk.Label(window, text="Please enter name to register (leave empty to skip):", font=("Helvetica", 10), bg="#f0f0f0")
regis_label.pack()

regis_entry = tk.Entry(window, font=("Helvetica", 10))
regis_entry.pack()

# Start the GUI event loop
window.mainloop()
