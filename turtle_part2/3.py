import turtle
import time

A = []

inp = open('3.txt', 'r')
for line in inp:
    B = list(map(int, line.split()))
    n = len(B)
    C = []
    for i in range(0, n, 2):
        C.append((B[i], B[i + 1]))
    A.append(C)
inp.close()

x = 0
y = 0
for a in A:
    turtle.penup()
    for (dx, dy) in a:
        turtle.goto(x + dx * 10, dy * 10)
        turtle.pendown()
    x += 20

time.sleep(10)
