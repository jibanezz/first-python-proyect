import turtle 
from brick import Brick
from rod import Platform
from ball import Ball
b1 = Brick()
b1.create_bricks()



platform = Platform((0, -200))


turtle.listen()
turtle.onkeypress(platform.start_moving_left, "Left")
turtle.onkeyrelease(platform.stop_moving_left, "Left")

turtle.onkeypress(platform.start_moving_right, "Right")
turtle.onkeyrelease(platform.stop_moving_right, "Right")


ball = Ball()
while True:
    ball.move()
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.reverse_y() 
    if ball.xcor() > 308 or ball.xcor() < -308:
        ball.reverse_x()




turtle.mainloop()




