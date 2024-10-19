from turtle import Turtle
from random import randint


class Snake:
    segment_positions = [(0, 0), (-20, 0), (-40, 0)]
    snake_segments = []
    WIDTH, HEIGHT = 720, 720

    def __init__(self, snake_screen):
        self.snake_screen = snake_screen

    def turn_up(self):
        if int(self.snake_segments[0].heading()) != 270:
            self.snake_segments[0].setheading(90)
            self.snake_screen.update()

    def turn_down(self):
        if int(self.snake_segments[0].heading()) != 90:
            self.snake_segments[0].setheading(270)
            self.snake_screen.update()

    def turn_left(self):
        if int(self.snake_segments[0].heading()) != 0:
            self.snake_segments[0].setheading(180)
            self.snake_screen.update()

    def turn_right(self):
        if int(self.snake_segments[0].heading()) != 180:
            self.snake_segments[0].setheading(0)
            self.snake_screen.update()

    def generate_body(self):
        for segment_position in self.segment_positions:
            segment = Turtle("square")
            segment.color("White")
            segment.penup()
            segment.goto(segment_position)
            self.snake_segments.append(segment)

    def grow_body(self, snake_segments):
        segment = Turtle("square")
        segment.color("White")
        segment.penup()
        segment.goto(snake_segments[-1].position())
        snake_segments.append(segment)

    def generate_food(self, food):
        food_position = (randint(-self.WIDTH // 2, self.HEIGHT // 2), randint(-self.WIDTH // 2, self.HEIGHT // 2))
        food.shape("circle")
        food.color("green")
        food.penup()
        food.xcor()
        food.goto(food_position)