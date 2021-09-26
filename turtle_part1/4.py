import turtle
import time
import numpy

n = int(input('number of sides'))
angle = 360 / n
l = 200 * numpy.pi / n
for i in range(n):
    turtle.forward(l)
    turtle.left(angle) 

time.sleep(10)
