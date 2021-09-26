import turtle
import time
import numpy

n = int(input('number of cycles'))
l = 10
for j in range (2 * n):
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    l = l + 10

time.sleep(10)
