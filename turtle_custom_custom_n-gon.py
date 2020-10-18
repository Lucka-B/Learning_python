from turtle import forward, shape, left, exitonclick, penup, pendown
from turtle import speed
pocet_stran = int(input("Zadej prosím počet stran: "))
speed(0)
shape('turtle')
strana = 200/(pocet_stran)
uhel = 180 * (2/(pocet_stran))
for i in range(pocet_stran):
    forward(strana)
    left(uhel)
exitonclick()
