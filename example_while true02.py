from turtle import Turtle, colormode
from random import randint
t = Turtle()
colormode(255)
t.speed(100000)
while True:
    t.penup()
    t.goto(randint(-250, 250), randint(-250, 250))
    t.pendown()
    a = 1
    r = randint(1, 100)
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.begin_fill()
    while a <= 4:
        t.forward(r)
        t.left(90)
        a += 1
    t.end_fill()
