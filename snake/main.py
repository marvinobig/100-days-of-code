import time
from turtle import Turtle, Screen
from snake import Snake
from collision import Collision
from score import Score


# Setup screen
snake_screen = Screen()
snake_screen.setup(720, 720)
snake_screen.title("Snake")
snake_screen.bgcolor("black")
snake_screen.tracer(0)
snake_screen.listen()

# Setup snake
snake = Snake(snake_screen)

# Setup snake food
snake_food = Turtle()
snake.generate_food(snake_food)

# Setup snake default body
snake.generate_body()

# Setup scoreboard
scoreboard = Score(snake_screen)
score = Turtle(visible=False)

# Setup collision
collision = Collision(snake_screen)


while True:
    snake_screen.update()
    time.sleep(0.1)

    snake.move()

    scoreboard.display_scores(score)

    collision.snake_food_collision(snake_food, scoreboard.increment)

    if collision.snake_body_collision():
        scoreboard.update_highscore(score)
        snake.reset()

    if collision.snake_wall_collision():
        scoreboard.update_highscore(score)
        snake.reset()

    # Setup control events
    snake_screen.onkeypress(snake.turn_up, "Up")
    snake_screen.onkeypress(snake.turn_down, "Down")
    snake_screen.onkeypress(snake.turn_left, "Left")
    snake_screen.onkeypress(snake.turn_right, "Right")
