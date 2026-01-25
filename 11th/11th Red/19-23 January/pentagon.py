import turtle

polygon = turtle.Turtle()

sides = 6

angle = 360/sides

for i in range(sides):
    polygon.forward(100)
    polygon.right(angle)

turtle.done()