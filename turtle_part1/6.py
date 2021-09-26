import turtle
import time
#import numpy

n = int(input('number of paws'))
angle = 360 / n
for i in range (n):
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(180 - angle)

time.sleep(10)
