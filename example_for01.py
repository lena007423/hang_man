from tle import  tle , done
t = tle ()

for i in range(4):
    t.pencolor("#FBC02D")
    t.forward(200)
    t.left(90) 
done()