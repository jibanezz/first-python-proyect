import turtle
import random


class Jose_turtle(turtle.Turtle):
    def __init__(self,color):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.penup()
    def getReady(self,x,y):
        self.goto(x,y)

    def run(self):
        self.forward(random.randint(1,10))
    

        