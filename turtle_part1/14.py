import turtle
import time

def star(n):
    angle = 180 * (n - 1) / n
    for i in range(n):
        turtle.forward(100)
        turtle.right(angle)

turtle.penup()
turtle.backward(200)
turtle.pendown()
star(5)
turtle.penup()
turtle.forward(200)
turtle.pendown()
star(11)

time.sleep(10)
