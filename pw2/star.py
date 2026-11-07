import turtle
import math

t = turtle.Turtle()

window = turtle.Screen()

def drawStar(numPoints : int, radius : float, color, doFill : bool):
    global t
    numPoints = numPoints - 1 if numPoints % 2 == 0 else numPoints
    if (doFill) :
        t.begin_fill()
    t.color(color)
    origin = t.pos()
    t.penup()
    angle = 0.0
    for i in range(0, numPoints * 2 + 1):
        radMult : float = 1 if i % 2 == 0 else 0.5
        t.goto((math.sin(angle) * radius * radMult + origin[0], math.cos(angle) * radius * radMult + origin[1]))
        t.pendown()
        angle += math.pi / numPoints
    t.penup()
    t.end_fill()
    t.goto(origin)

t.penup()
t.goto(-120, 0)
drawStar(5, 50, (0, 0, 0), True)
t.goto(0, 0)
drawStar(15, 50, (1, 0, 0), False)
t.goto(120, 0)
drawStar(8, 50, (0.8, 0.8, 0), True)

window.exitonclick()