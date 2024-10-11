import pgzrun
from random import randint
WIDTH=500
HEIGHT=500
TITLE='box'
box1=Rect((0,0),(25,25))
box2=Rect((400,400),(25,25))
vx=1
vy=1
vx1=1
vy1=1
def draw():
    screen.clear()
    screen.fill('black')
    screen.draw.filled_rect(box1,'red')
    screen.draw.filled_rect(box2,'blue')

def update():
    global vx, vy,vx1,vy1
    box1.x+=vx
    box1.y+=vy
    if box1.x>475 or box1.x<0:
        vx=-vx
    if box1.y>475 or box1.y<0:
        vy=-vy
    box2.x+=vx1
    box2.y+=vy1
    if box2.x>475 or box2.x<0:
        vx1=-vx1
    if box2.y>475 or box2.y<0:
        vy1=-vy1

pgzrun.go()
