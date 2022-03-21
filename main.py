list_of_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    list_of_colors.append(new_color)

tim = Turtle()
turtle.colormode(255)
tim.speed('fastest')
tim.penup()
tim.hideturtle()
tim.setheading(220)
tim.forward(300)
tim.setheading(0)

for dots in range(1, 401):
    color = random.choice(list_of_colors)
    tim.dot(10, color)
    tim.forward(20)

    if dots%20 == 0:
        tim.left(90)
        tim.forward(20)
        tim.left(90)
        tim.forward(400)
        tim.setheading(0)

my_screen = Screen()
my_screen.exitonclick()
