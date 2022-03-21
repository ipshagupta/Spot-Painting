#This a sub-program file that uses the turtle module to create shapes like a square, pentagon, hexagon, heptagon, etc.

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')


def draw_shape(n):
    angle = 360/n
    for _ in range(0, n):
        timmy.forward(50)
        timmy.right(angle)


timmy.color('blue', 'blue')
timmy.begin_fill()
draw_shape(4)
timmy.end_fill()

timmy.color('red', 'red')
timmy.begin_fill()
draw_shape(5)
timmy.end_fill()

timmy.color('green', 'green')
timmy.begin_fill()
draw_shape(6)
timmy.end_fill()

timmy.color('yellow', 'yellow')
timmy.begin_fill()
draw_shape(7)
timmy.end_fill()

timmy.color('orange', 'orange')
timmy.begin_fill()
draw_shape(8)
timmy.end_fill()
my_screen = Screen()
my_screen.exitonclick()
