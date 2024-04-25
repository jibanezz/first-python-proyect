# challenge
"""
make a turtle which will randomly walk for steps between 1 to 10 and will randomle chose angle between 0 to 360
step = random.randint(1,10)
ang = random.randint(0,360)
.forward(step)
"""
import turtle 
import random

tim = turtle.Turtle()
all_turtles = []
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for i in range(8):
    tim = turtle.Turtle()
    tim.pensize(10)
    tim.color(colours[i])
    all_turtles.append(tim)

d = [0,90,180,270]


for i in range(50):
    for tim in all_turtles:
        step = random.randint(50,100)
        ang = random.choice(d)
        #tim.color(random.choice(colours))
        tim.forward(step)
        tim.left(ang)
        