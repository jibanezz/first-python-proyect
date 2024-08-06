import turtle
import random

class Brick ():
    def __init__(self):
        self.bricks = []

    def create_bricks(self):
        x_positons = [-200, -150, -100, -50,0, 50, 100, 150, 200]
        colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple','black','pink' ,'red' ]
        y_positions = [200,175,150,125]
        for y in y_positions:
            color = random.choice(colors)
            for x in x_positons:
                self.bricks.append(turtle.Turtle())
                self.bricks[-1].speed(0)
                self.bricks[-1].shape('square')
                self.bricks[-1].color(color)
                self.bricks[-1].penup()
                self.bricks[-1].goto(x, y)
                self.bricks[-1].shapesize(stretch_len=2, stretch_wid=1)



if __name__ == '__main__':
    b1 = Brick()
    b1.create_bricks()


    turtle.mainloop()