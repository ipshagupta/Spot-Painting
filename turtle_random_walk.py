#This is a sub-file to test and program a random path by using turtle graphics.

import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
direction = [0, 90, 180, 270]

tim.speed('fastest')
tim.width(7)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


for _ in range(100):
    tim.forward(25)
    tim.color(random_color())
    tim.setheading(random.choice(direction))

my_screen = Screen()
my_screen.exitonclick()
