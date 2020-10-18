from turtle import forward, right, left, shape, speed, exitonclick, circle,
shape('turtle')
speed(0)
# květ
for i in range(18):
    for j in range(4):
        forward(50)
        left(90)
    left(20)
# stonek a listy
right(90)
forward(100)
for i in range(12):
    if i % 2 == 0:
        left(75)
        circle(50 + i * 3, 70)
        left(110)
        circle(50 + i * 3, 70)
        left(35)
    else:
        right(75)
        circle(-50 - i * 3, 70)
        right(110)
        circle(-50 - i * 3, 70)
        right(35)
    forward(20)
exitonclick()
