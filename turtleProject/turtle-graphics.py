from turtle import Turtle, Screen
import heroes

ttl = Turtle()

ttl.shape('turtle')
ttl.color('red')

def square(size):
    for i in range(4):
        ttl.forward(size)
        ttl.right(90)

def dashed_line(dash_length, distance):
    for i in range(distance):
        ttl.down()
        ttl.forward(dash_length)
        ttl.up()
        ttl.forward(dash_length)
    ttl.down()

def rectangle(size):
    for i in range(4):
        if i == 1 or i == 3:
            ttl.forward(size)
        else:
            ttl.forward(size * 2)

        ttl.right(90)


# dashed_line(5, 10)
# square(100)
rectangle(100)
ttl_screen = Screen()
ttl_screen.exitonclick()

# print(heroes.gen())
