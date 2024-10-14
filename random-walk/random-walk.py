from turtle import Turtle, Screen, colormode
from random import randint


DIRECTIONS = [-90, 90]
FORWARD_STEPS = 60
WIDTH, HEIGHT = 720, 720
BOUNDARY_X = WIDTH // 2 - 10  # Screen boundary for X - pen width
BOUNDARY_Y = HEIGHT // 2 - 10  # Screen boundary for Y - pen width

colormode(255)
rnd_walk = Turtle()
rnd_walk_screen = Screen()

rnd_walk.shape('circle')
rnd_walk.pensize(10)
rnd_walk_screen.title("Random Walk")
rnd_walk_screen.setup(WIDTH, HEIGHT)


def check_boundary(turtle):
    x, y = turtle.xcor(), turtle.ycor()

    if x > BOUNDARY_X:
        turtle.setheading(180)  # Move left
    elif x < -BOUNDARY_X:
        turtle.setheading(0)  # Move right
    elif y > BOUNDARY_Y:
        turtle.setheading(270)  # Move down
    elif y < -BOUNDARY_Y:
        turtle.setheading(90)  # Move up


for walks in range(randint(50, 250)):
    colours = (randint(0, 255), randint(0, 255), randint(0, 255))

    rnd_walk.color(colours)
    rnd_walk.right(DIRECTIONS[randint(0, 1)])
    check_boundary(rnd_walk)

    rnd_walk.forward(FORWARD_STEPS)


rnd_walk_screen.exitonclick()
