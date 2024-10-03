import turtle 
class Ball(turtle.Turtle):
    def __init__(self,speed):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.radius = 10
        self.dx = speed
        self.dy = speed

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def reverse_x(self):
        self.dx *= -1
        self.color('blue')

    def reverse_y(self):
        self.dy *= -1
        self.color('green')

if __name__ == "__main__":
    ball = Ball()
    while True:
        ball.move()
        if ball.ycor() > 250 or ball.ycor() < -250:
            ball.reverse_y() 
        if ball.xcor() > 308 or ball.xcor() < -308:
            ball.reverse_x()

     

