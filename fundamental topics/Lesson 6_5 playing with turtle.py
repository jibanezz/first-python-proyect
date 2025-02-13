
import turtle 

c1 = turtle.Turtle()
c2 = turtle.Turtle()
c1.speed("fastest")
c2.speed(1000)

for i in range(50):

    c1.shape('turtle')
    c1.forward(100)
    c1.left(90)
    c1.forward(100)
    c1.left(90)
    c1.forward(100)
    c1.left(90)
    c1.forward(100)
    c1.left(90)
    c1.left(5)


    c2.shape('turtle')
    c2.color('red')
    c2.forward(100)
    c2.left(120)
    c2.forward(100)
    c2.left(120)
    c2.forward(100)
    c2.left(120)
    c2.left(5)


turtle.mainloop()