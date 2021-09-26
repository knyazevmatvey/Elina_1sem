import turtle
import time

A = []
A.append([(0, 1), (1, 2), (1, 0)])
A.append([(0, 2), (0, 1), (1, 1), (1, 2), (1, 0)])
A.append([(0, 1), (1, 2), (1, 0)])
A.append([(0, 0), (0, 1), (1, 2), (0, 2)])
A.append([(0, 0), (0, 2), (1, 2), (1, 0), (0, 0)])
A.append([(0, 0), (0, 2), (1, 2), (1, 0), (0, 0)])
x = 0
y = 0
for a in A:
    turtle.penup()
    for (dx, dy) in a:
        turtle.goto(x + dx * 10, dy * 10)
        turtle.pendown()
    x += 20

time.sleep(10)
