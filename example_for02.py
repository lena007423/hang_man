from turtle import Turtle , done
from random import randint
t = Turtle()
for i in range(20):
    t.penup()
    x = randint(-250, 250)
    y = randint(-250, 250)
    r = randint(10, 60)
    t.goto(x, y)
    t.pendown()
    t.color("rad")
    t.circle(r)

done()