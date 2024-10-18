import time
from turtle import Turtle, Screen
from random import randint
from snake import Snake


def generate_food(food):
    food_position = (randint(-WIDTH // 2, HEIGHT // 2), randint(-WIDTH // 2, HEIGHT // 2))
    food.shape("circle")
    food.color("green")
    food.penup()
    food.xcor()
    food.goto(food_position)

def snake_food_collision(snake, food, generate_food_function):
    if snake.distance(food) < 20:
        generate_food_function(food)

# Screen size
WIDTH, HEIGHT = 720, 720

# Configure screen
snake_screen = Screen()
snake_screen.setup(WIDTH, HEIGHT)
snake_screen.title("Snake")
snake_screen.bgcolor("black")
snake_screen.tracer(0)

snake_screen.listen()

# Generate food
snake_food = Turtle()
generate_food(snake_food)

# Configure snake default body
segment_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []
playing = True

for segment_position in segment_positions:
    segment = Turtle("square")
    segment.color("White")
    segment.penup()
    segment.goto(segment_position)
    snake_segments.append(segment)

while playing:
    snake_screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake_segments) - 1, 0, -1):
        new_xcor = snake_segments[seg_num - 1].xcor()
        new_ycor = snake_segments[seg_num - 1].ycor()
        snake_segments[seg_num].goto(new_xcor, new_ycor)

    snake_segments[0].forward(20)
    snake_food_collision(snake_segments[0], snake_food, generate_food)

    # Control events
    snake_controls = Snake(snake_segments[0], snake_screen, WIDTH, HEIGHT)
    snake_screen.onkeypress(snake_controls.up, "Up")
    snake_screen.onkeypress(snake_controls.down, "Down")
    snake_screen.onkeypress(snake_controls.left, "Left")
    snake_screen.onkeypress(snake_controls.right, "Right")



snake_screen.mainloop()





