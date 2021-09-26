import turtle
import time
import numpy

def figure(n, r0, r):
    phi = 360 / n
    a = 2 * r * numpy.sin(phi / 360 * numpy.pi)
    turtle.left(phi + 90 * (n - 2) / n)
    for j in range (n):
        turtle.forward(a)
        turtle.left(phi)
    turtle.right(phi + 90 * (n - 2) / n)
    turtle.penup()
    turtle.forward(r0)
    turtle.pendown()

r0 = 10
for i in range(1, 11, 1):
    r = r0 * i
    n = i + 2
    figure(n, r0, r)

time.sleep(10)
