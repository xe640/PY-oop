import turtle
import math

t = turtle.Turtle()

window = turtle.Screen()

def axis():
    t.color(0.5,0,0.5)
    t.pendown()
    for i in range(2):
        t.forward(165)
        for i in range(2):
            t.right(135)
            t.forward(4)
            t.right(180)
            t.forward(4)
            t.right(135)
        t.forward(330)
        t.right(180)
        t.forward(165)
        t.left(90)
    for i in range(-3,4):
        t.penup()
        t.goto(3,50*i)
        t.pendown()
        t.goto(-3,50*i)
    for i in range(-3,4):
        t.penup()
        t.goto(50*i,3)
        t.pendown()
        t.goto(50*i,-3)
    t.penup()
    t.goto(0,0)
def funct():
        t.color(0,0,0.3)   
        for x in range (-160,161):
             t.goto(x,(x/5)+27)
             t.pendown()

axis()
funct()

window.exitonclick()