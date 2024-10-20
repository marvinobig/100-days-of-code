import time
from turtle import Turtle, Screen
from snake import Snake
from collision import Collision
from score import Score


# Configure screen
snake_screen = Screen()
snake_screen.setup(720, 720)
snake_screen.title("Snake")
snake_screen.bgcolor("black")
snake_screen.tracer(0)
snake_screen.listen()

# Snake
snake = Snake(snake_screen)

# Generate food
snake_food = Turtle()
snake.generate_food(snake_food)

# Configure snake default body
snake.generate_body()

# Scoreboard
scoreboard = Score(snake_screen)
score = Turtle(visible=False)


while True:
    snake_screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake.snake_segments) - 1, 0, -1):
        new_xcor = snake.snake_segments[seg_num - 1].xcor()
        new_ycor = snake.snake_segments[seg_num - 1].ycor()
        snake.snake_segments[seg_num].goto(new_xcor, new_ycor)

    snake.snake_segments[0].forward(20)

    scoreboard.display_score(score)

    collision = Collision(snake_screen)
    collision.snake_food_collision(snake_food, scoreboard.increment)

    if collision.snake_body_collision():
        snake.game_over()
        break

    if collision.snake_wall_collision():
        snake.game_over()
        break

    # Control events
    snake_screen.onkeypress(snake.turn_up, "Up")
    snake_screen.onkeypress(snake.turn_down, "Down")
    snake_screen.onkeypress(snake.turn_left, "Left")
    snake_screen.onkeypress(snake.turn_right, "Right")


snake_screen.mainloop()





