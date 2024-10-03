"""
1. you can actually use RGB colors 
r = random.randint(0,255)

g = random.randint(0,255)

b = random.randint(0,255)

t = (r,g,b)

tim.color(t)


"""



import turtle
import random
tim = turtle.Turtle()
turtle.colormode(255)
tim.pensize(6)
tim.speed('fastest')
for i in range (360/5):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    t = (r,g,b)
    tim.color(t)
    tim.forward(2.5)
    tim.left(1)


turtle.mainloop()