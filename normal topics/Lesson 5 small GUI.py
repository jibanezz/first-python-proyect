# 1 tinkercad

import tkinter as tk 
root = tk.Tk()
root.title("Jose Calculator")
jose1 = tk.Entry(root)
jose1.grid(row=1, column=1,padx=5 , pady=10)
jose2 = tk.Entry(root)
jose2.grid(row=1, column=2)

jose3 = tk.Entry(root)
jose3.grid(row=1, column=3)

l1 = tk.Label(root,text = "number1")
l1.grid(row=2, column=1)

l1 = tk.Label(root,text = "operator")
l1.grid(row=2, column=2)

l1 = tk.Label(root,text = "number2")
l1.grid(row=2, column=3)

def fun():
    print("fun")
    x = jose1.get()
    op = jose2.get()
    y = jose3.get()
    print(x,op,y)
    ans = x+op+y
    ans = eval(ans)
    jose5.config(text=ans)
    

jose4 = tk.Button(root,text="submit",command=fun)
jose4.grid(row=3, column=2)

jose5 = tk.Label(root,text="i am results")
jose5.grid(row=4, column=2)


button1 = tk.Button(root, text="1", width=5, height=2)
button1.grid(row=5, column=1)
    
button2 = tk.Button(root, text="2", width=5, height=2)
button2.grid(row=5, column=2)
    
button3 = tk.Button(root, text="3", width=5, height=2)
button3.grid(row=5, column=3)
    

button = tk.Button(root, text="4", width=5, height=2)
button.grid(row=6, column=1)
    
button = tk.Button(root, text="5", width=5, height=2)
button.grid(row=6, column=2)
    
button = tk.Button(root, text="6", width=5, height=2)
button.grid(row=6, column=3)
    


tk.mainloop()