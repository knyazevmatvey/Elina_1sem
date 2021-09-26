import turtle
import time
import numpy

l = 10
r = 5 * numpy.sqrt(2)
for i in range(10):
    for j in range(4):
        turtle.forward(l)
        turtle.left(90)
    turtle.right(135)
    turtle.penup()
    turtle.forward(r)
    turtle.pendown()
    turtle.left(135)
    l = l + 10

time.sleep(10)
