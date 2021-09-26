import turtle
import time

def circle(r):
    n = 360
    angle = 360 / n
    l = 2 * r * 3.1415 / n
    for i in range(n):
        turtle.forward(l)
        turtle.left(angle)

def f(d):
    n = 180
    angle = 360 / n
    l = d * 3.1415 / n
    for i in range(90):
        turtle.forward(l)
        turtle.right(angle)


turtle.color('black', 'yellow')
turtle.begin_fill()
circle(100)
turtle.end_fill()

turtle.left(90)
turtle.penup()
turtle.forward(130)
turtle.left(90)
turtle.forward(40)
turtle.left(180)
turtle.pendown()
turtle.color('black', 'blue')
turtle.begin_fill()
circle(10)
turtle.end_fill()
turtle.penup()
turtle.forward(80)
turtle.pendown()
turtle.color('black', 'blue')
turtle.begin_fill()
circle(10)
turtle.end_fill()

turtle.left(180)
turtle.penup()
turtle.forward(40)
turtle.left(90)
turtle.forward(15)
turtle.pendown()
turtle.width(5)
turtle.forward(30)
turtle.penup()
turtle.forward(10)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.pendown()

turtle.width(7)
turtle.color('red')
f(100)

time.sleep(10)
