
import turtle as t
import random
t.speed('fastest')
tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())#choose
        tim.circle(100)# make circle
        tim.setheading(tim.heading() + size_of_gap) # set head positon with old + 5

draw_spirograph(5)