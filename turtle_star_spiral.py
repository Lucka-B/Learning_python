from random import randrange
from turtle import forward, shape, right, exitonclick, left, penup, pendown
from turtle import speed
speed(0)
shape('turtle')
for i in range(200):
    penup()
    forward(i/2)
    left(15)
    pendown()
    left(15)
    for j in range(5):
        forward(0.5 * i)
        right(180 - 35)
    right(15)
exitonclick()
