import turtle
import time
import numpy

def circle(r):
    n = 180
    angle = 360 / n
    l = 2 * r * numpy.pi / n
    for i in range(n):
        turtle.forward(l)
        turtle.left(angle)

k = int(input('number of circles'))
turtle.left(90)
r0 = 10
for i in range(1, k + 1, 1):
    r = r0 * i
    circle(r)
    turtle.right(180)
    circle(r)

time.sleep(10)
