import turtle
import time
import numpy

k = float(input('k'))
n = int(input('number of cycles'))
dphi = 1
phi = 0
m = int(360 / 10)
for j in range (m * n):
    dl = k * dphi * numpy.sqrt(1 + phi ** 2)
    turtle.forward(dl)
    turtle.left(10)
    phi = phi + dphi

time.sleep(10)
