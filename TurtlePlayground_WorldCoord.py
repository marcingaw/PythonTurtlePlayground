from turtle import *

def KochSnowflakeEdge(turtle, order, length):
    if order <= 0:
        turtle.forward(length)
        return
    KochSnowflakeEdge(turtle, order - 1, length)
    turtle.left(60)
    KochSnowflakeEdge(turtle, order - 1, length)
    turtle.right(120)
    KochSnowflakeEdge(turtle, order - 1, length)
    turtle.left(60)
    KochSnowflakeEdge(turtle, order - 1, length)

def KochSnowflake(turtle, order, length):
    for _ in range(3):
        KochSnowflakeEdge(turtle, order, length)
        turtle.right(120)

def SierpinskiTriangle(turtle, order, length):
    if order <= 0:
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(length)
            turtle.right(120)
        turtle.end_fill()
        return length
    move_by = SierpinskiTriangle(turtle, order - 1, length)
    turtle.forward(move_by)
    SierpinskiTriangle(turtle, order - 1, length)
    turtle.back(move_by)
    turtle.right(60)
    turtle.forward(move_by)
    turtle.left(60)
    SierpinskiTriangle(turtle, order - 1, length)
    turtle.right(60)
    turtle.back(move_by)
    turtle.left(60)
    return move_by + move_by

screen = Screen()
screen.setup(0.8, 0.8, None, None)
range_y = 500
range_x = int(screen.window_width() / screen.window_height() * range_y)
screen.setworldcoordinates(-range_x, -range_y, range_x, range_y)

turtle = Turtle()
turtle.speed(0)
turtle.color('black', 'grey')

turtle.penup()
turtle.setpos(-(0.8 * range_x), 0.8 * range_y)
turtle.pendown()
KochSnowflake(turtle, 4, 3)

turtle.penup()
turtle.setpos(0.2 * range_x, 0.8 * range_y)
turtle.pendown()
KochSnowflake(turtle, 3, 9)

turtle.penup()
turtle.setpos(-(0.8 * range_x), -(0.2 * range_y))
turtle.pendown()
SierpinskiTriangle(turtle, 5, 8)

turtle.penup()
turtle.setpos(0.2 * range_x, -(0.2 * range_y))
turtle.pendown()
SierpinskiTriangle(turtle, 4, 16)

done()
