import turtle 


c1 = turtle.Turtle()
# c1.speed(100)
# c1.forward(100)
# c1.left(90)
# c1.forward(90)
# c1.left(90)
# c1.forward(80)
# c1.left(90)
# c1.forward(70)  
# c1.left(90)
# c1.forward(60)
# c1.left(90)
# c1.forward(50)
# c1.left(90)
# c1.forward(40)
# c1.left(90)
# c1.forward(30) 
# c1.left(90)
# c1.forward(20)
# c1.left(90)
# c1.forward(20)
x = 10
end=300
d = 10
for i in range(x,end,d):
    c1.forward(i)
    c1.left(90)
turtle.mainloop()
# i added a comment