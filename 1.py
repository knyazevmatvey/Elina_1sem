import turtle
import time
from random import *

n = 15
for i in range(n):
    l = randint(10, 100)
    angle = randint(1, 360)
    turtle.forward(l)
    turtle.left(angle)

time.sleep(10)
