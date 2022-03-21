#Using turtle graphics, I have created a spirograph graphic in multiple colors

import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

tim.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def draw(size):
    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.left(size)


draw(5)

my_screen = Screen()
my_screen.exitonclick()
