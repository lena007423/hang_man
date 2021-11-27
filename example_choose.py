from turtle import*
sp = input("choose triangle ,square or rectangle:")

if sp == "square":
    forward (150)
    left(90)
    forward (150)
    left(90)
    forward (150)
    left(90)
    forward (150)
    left(90)
elif sp == "rectangle":
    forward (200)
    left(90)
    forward(100)
    left(90)
    forward (200)
    left(90)
    forward(100)
elif sp == "triangle":
    forward(150)
    left(120)
    forward(150)
    left(120)
    forward(150)
    
done()