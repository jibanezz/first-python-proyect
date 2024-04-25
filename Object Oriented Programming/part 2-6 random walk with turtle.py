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
timi = turtle.Turtle() # i made another object
all_turtles = []

d = [0,90,180,270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.pensize(15)
timi.pensize(10)
for i in range(50):
    step = random.randint(50,100)
    ang = random.choice(d)
    tim.color(random.choice(colours))
    tim.forward(step)
    tim.left(ang)
    
    step = random.randint(50,100)
    ang = random.choice(d)
    timi.color(random.choice(colours))
    timi.forward(step)
    timi.left(ang)



