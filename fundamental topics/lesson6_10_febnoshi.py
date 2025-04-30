import turtle
    
c1 = turtle.Turtle()
c1.speed(100)
s = 1
for i in range(1000):
    c1.forward(10)
    c1.left(s)
    s += 0.01



