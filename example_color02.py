from turtle import tle, done,colormode
from random import randint
t = tle()
colormode(255)
for i in range(100):
    t.penup()
    t.goto(randint(-250, 250), randint(-250, 250))
    t.pendown()
    a = 1
    r = randint(10, 100)
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.begin_fill()
    while a <= 4:
        t.forward(r)
        t.left(90)
        a += 1
    t.end_fill()
done()