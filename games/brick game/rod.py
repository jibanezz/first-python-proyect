import turtle


class Platform(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("blue")
        self.shapesize(1, 6 )
        self.speed(0)
        self.goto(position)
        self.is_moving_left = False
        self.is_moving_right = False

    def move_left(self):
        if self.is_moving_left:
            self.backward(5)
            if self.xcor() < -280:
                self.goto(-280, self.ycor())
            turtle.ontimer(self.move_left, 100)


    def start_moving_left(self):
        self.is_moving_left = True
        self.move_left()

    def stop_moving_left(self):
        self.is_moving_left = False
       



    def move_right(self):
        if self.is_moving_right:
            self.forward(5)
            if self.xcor() > 280:
                self.goto(280, self.ycor())
            turtle.ontimer(self.move_right, 100)

    def start_moving_right(self):
        self.is_moving_right = True
        self.move_right()

    def stop_moving_right(self):
        self.is_moving_right = False    


if __name__ == "__main__":
    platform = Platform((0, -200))

    turtle.listen()
    turtle.onkeypress(platform.start_moving_left, "Left")
    turtle.onkeyrelease(platform.stop_moving_left, "Left")

    turtle.onkeypress(platform.start_moving_right, "Right")
    turtle.onkeyrelease(platform.stop_moving_right, "Right")


    turtle.mainloop()



