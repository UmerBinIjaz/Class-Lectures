import turtle

mf = turtle.Turtle()
mf.speed(5)
mf.pencolor("red")
mf.width(3)

mf.begin_fill()
mf.fillcolor("yellow")

for _ in range(5):
    mf.forward(100)
    mf.right(144)

mf.end_fill()
turtle.done()