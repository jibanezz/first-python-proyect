import turtle 
from brick import Brick
from rod import Platform
from ball import Ball
b1 = Brick()


turtle.tracer(0)
b1.create_bricks([150,200],[-200,300])



platform = Platform((0, -200))


turtle.listen()
turtle.onkeypress(platform.start_moving_left, "Left")
turtle.onkeyrelease(platform.stop_moving_left, "Left")

turtle.onkeypress(platform.start_moving_right, "Right")
turtle.onkeyrelease(platform.stop_moving_right, "Right")


ball = Ball(0.2)
num = 1
while True:
    ball.move()
    if ball.ycor() > 250:
        ball.reverse_y() 
    if ball.xcor() > 308 or ball.xcor() < -308:
        ball.reverse_x()
    if ball.ycor() < -308:
        turtle.write("Game Over!", align="center", font=("Courier", 48, "normal"))
        turtle.done()
    if (ball.ycor() - platform.ycor()) < 50:
        if (ball.xcor() -platform.xcor()) < 50:
            ball.reverse_y()

    for brick in b1.bricks:
        if ball.distance(brick) < 40:
            brick.hideturtle()
            ball.reverse_y()
            b1.bricks.remove(brick)
            break
    if len(b1.bricks) == 0:
        turtle.write (f"Level {num} achievedPress any key to continue", align="center", font=("Courier", 24,) )
        b1.create_bricks([100,200],[-200,0,100])
    turtle.update()


turtle.mainloop()




