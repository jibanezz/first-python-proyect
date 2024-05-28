# tkinter
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk("Jose game of jumping")
# set side to 500x500

root.geometry("700x700")

#create canvas

canvas = tk.Canvas(root, width=700, height=700)
canvas.pack()
# i want to add background picture ImageTk
bgimage = ImageTk.PhotoImage(Image.open("games/A game of jumping rabit/photos/gf.jpg"))
bg = canvas.create_image(0, 0, image=bgimage)

oi = Image.open("games/A game of jumping rabit/photos/bny.png").resize((200,200))
rbtimage = ImageTk.PhotoImage(oi)
rbt = canvas.create_image(200,200,image = rbtimage)

# make rbt jumping on presssing space button



def start_jump(event):
    canvas.move(rbt, 0, -10)




root.bind("<KeyPress-space>", start_jump)

# keep rbt falling

def fall():
    canvas.move(rbt, 0, 10)
    root.after(100, fall)
    canvas.move(rbt, 0, 10)

root.after(100, fall)

root.mainloop()



