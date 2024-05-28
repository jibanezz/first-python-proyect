import tkinter as tk

w = tk.Tk()

jose_text  = tk.Text(w, height=10, width=50)
jose_text.pack()

Button = tk.Button(w, text="Click me", command=lambda: jose_text)
                   


w.mainloop()

