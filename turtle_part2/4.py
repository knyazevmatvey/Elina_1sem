import turtle
import time

Vx = 4
Vy = 20
ay = -2
dt = 1
x = 0
y = 0
deltaV = 2

n = int(Vy / deltaV)
for i in range (n):
    for j in range (int(Vy * 2 / abs(ay))):
        x += Vx * dt
        y += Vy * dt + ay * (dt ** 2) / 2
        Vy += ay * dt
        turtle.goto(x, y)
    Vy = -Vy - deltaV

time.sleep(10)
