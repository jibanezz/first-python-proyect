# to understand the concept of classes in details

import turtle
from random import randint
from myturtle import Jose_turtle
import time
from scipy.stats import rankdata
        
turtle_list = []
colors = ['red', 'green', 'blue', 'purple', 'yellow', 'cyan','pink']
y_list = [-300,-200,-100,0,100,200,300]

for c,y in zip(colors,y_list):
    t = Jose_turtle(color = c)
    t.getReady(-400,y)
    turtle_list.append(t)                   

turtle.tracer(0)

while True:   
    positons = []
    for each in turtle_list:
        each.run()
        time.sleep(0.01)
        positons.append(each.xcor())
        

    turtle.Screen().update()
    if max(positons) > 400:
        # find winner
        ranks = rankdata(positons)
        for i in range(len(ranks)):
            turtle_list[i].write(f'Mr. {colors[i]}  has rank {ranks[i]}')
        break

turtle.mainloop()
