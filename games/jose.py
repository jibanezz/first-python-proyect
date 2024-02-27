import pgzrun
import random
WIDTH = 800
HEIGHT = 600

stars = []
# for changing the background color
player = Actor('jose2')
player.pos = (400,550)
def draw():
    screen.fill([0,0,0])
    player.draw()
    for star in stars:
        star.draw()
def update():
    for star in stars:
        star.y += 2
        if star.colliderect(player):
            stars.remove(star)
    if keyboard.left:
        player.x -= 5
    elif keyboard.right:
        player.x += 5
    if player.left < 0:
        player.left = 0
    elif player.right > WIDTH:
        player.right = WIDTH



def create_star():
    star  = Actor('star')
    star.pos = (random.randint(50,WIDTH-50) , 0 )
    stars.append(star)


clock.schedule_interval(create_star,1)

pgzrun.go()