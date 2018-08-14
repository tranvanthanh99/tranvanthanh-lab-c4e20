from turtle import *
def draw_square(x,y):
    color(y)
    speed(-1)
    for i in range(4):
        forward(x)
        left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
