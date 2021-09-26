import turtle
import time
import numpy

def circle():
    n = 360
    angle = 360 / n
    l = 200 * numpy.pi / n
    for i in range(n):
        turtle.forward(l)
        turtle.left(angle)

k = int(input('number of circles'))
phi = 360 / k
for i in range(k):
    circle()
    turtle.right(phi)

time.sleep(10)
