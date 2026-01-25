import turtle

mult_square =  turtle.Turtle()

def multiple_squares(length, color):
    mult_square.begin_fill()
    mult_square.fillcolor("#5BE552")
    mult_square.pencolor(color)
    mult_square.pensize(2)
    mult_square.forward(length)
    mult_square.right(90)
    mult_square.forward(length)
    mult_square.right(90)
    mult_square.forward(length)
    mult_square.right(90)
    mult_square.forward(length)
    mult_square.right(90)
    mult_square.end_fill()

    mult_square.setheading(360) # 0: right, 90: Up, 180: Left, 270: down, 360: right

for i in range(60, 120, 15):
    multiple_squares(i, "blue")

# turtle.done()