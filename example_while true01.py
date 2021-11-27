from turtle import Turtle, colormode
from random import randint
colormode (255)
t = Turtle()

while True :
    t.penup()
    x = randint(-250, 250)
    y = randint(-250, 250)
    t.goto(x, y)
    t.pendown()
    r = randint(10, 100)
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.begin_fill()
    t.circle(r)
    t.end_fill()