import turtle 
c1 = turtle.Turtle()

step = 100
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
c1.speed(100)
for i in range(100):

    c1.forward(step)
    c1.left(90)
    c1.forward(90)
    step = step - 1
    c1.color(colors[i%6])


c1.forward(10)
turtle.mainloop()