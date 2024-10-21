from turtle import Turtle
from random import randint


class Snake:
    segment_positions = [(0, 0), (-20, 0), (-40, 0)]
    snake_segments = []
    WIDTH, HEIGHT = 720, 720

    def __init__(self, snake_screen):
        self.snake_screen = snake_screen

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_xcor = self.snake_segments[seg_num - 1].xcor()
            new_ycor = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_xcor, new_ycor)

        self.snake_segments[0].forward(20)

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
        left_boundary = (-self.WIDTH  // 2) + 20
        up_boundary = (self.HEIGHT // 2) - 20

        food_position = (randint(left_boundary, up_boundary), randint(left_boundary, up_boundary))
        food.shape("circle")
        food.color("green")
        food.penup()
        food.xcor()
        food.goto(food_position)

    def reset(self):
        for segment in self.snake_segments:
            segment.goto(self.WIDTH * 2, self.HEIGHT * 2)

        self.snake_segments.clear()
        self.generate_body()