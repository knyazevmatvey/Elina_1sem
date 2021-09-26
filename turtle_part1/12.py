import turtle
import time
import numpy

def f(d):
    n = 180
    angle = 360 / n
    l = d * numpy.pi / n
    for i in range(90):
        turtle.forward(l)
        turtle.right(angle)

k = int(input('number of curls'))
turtle.left(90)
for i in range(1, k + 1, 1):
    f(30)
    f(10)
f(30)

time.sleep(10)
