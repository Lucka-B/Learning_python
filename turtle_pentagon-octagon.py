from turtle import forward, shape, left, exitonclick, penup, pendown
from turtle import speed
speed(0)
shape('turtle')
for n in range(4):
    strana = 200/(n+5)
    uhel = 180 * (2/(n+5))
    for i in range(n+5):
        forward(strana)
        left(uhel)
    penup()
    forward(80)
    pendown()
exitonclick()