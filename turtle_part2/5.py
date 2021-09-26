
from random import randint
import turtle

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
turtle.forward(400)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(400)
turtle.right(90)

number_of_turtles = 13
steps_of_time_number = 100


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))

Vx = []
for i in range(number_of_turtles):
    Vx.append(randint(2, 10))

Vy = []
for i in range(number_of_turtles):
    Vy.append(randint(2, 10))

for i in range(steps_of_time_number):
    for j in range(number_of_turtles):
        x = pool[j].xcor()
        y = pool[j].ycor()
        if 190 <= abs(x) <= 210:
            Vx[j] = -Vx[j]
        if 190 <= abs(y) <= 210:
            Vy[j] = -Vy[j]
        pool[j].goto(x + Vx[j], y + Vy[j])
        



