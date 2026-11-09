import turtle
import math

t = turtle.Turtle()

window = turtle.Screen()

def axis():
    t.pendown
    t.forward(165)
    t.right(135)
    t.forward(2)
    t.right(180)
    t.forward(2)
    t.left(90)
    t.forward(2)
    t.left(180)
    t.forward(2)
    t.right(135)
    t.forward(330)
    t.right(180)
    t.forward(165)
    t.right(90)

axis

window.exitonclick()