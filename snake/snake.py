class Snake:
    def __init__(self, snake_head, snake_screen, screen_width, screen_height):
        self.snake_head = snake_head
        self.snake_screen = snake_screen
        self.screen_width = screen_width
        self.screen_height = screen_height

    def up(self):
        self.snake_head.setheading(90)
        self.check_boundary()
        self.snake_screen.update()

    def down(self):
        self.snake_head.setheading(270)
        self.check_boundary()
        self.snake_screen.update()

    def left(self):
        self.snake_head.setheading(180)
        self.check_boundary()
        self.snake_screen.update()

    def right(self):
        self.snake_head.setheading(0)
        self.check_boundary()
        self.snake_screen.update()

    def check_boundary(self):
        x, y = self.snake_head.xcor(), self.snake_head.ycor()
        boundary_x = self.screen_width // 2
        boundary_y = self.screen_height // 2

        if x > boundary_x:
            self.snake_head.setheading(180)  # Move left
            self.snake_screen.update()
        elif x < -boundary_x:
            self.snake_head.setheading(0)  # Move right
            self.snake_screen.update()
        elif y > boundary_y:
            self.snake_head.setheading(270)  # Move down
            self.snake_screen.update()
        elif y < -boundary_y:
            self.snake_head.setheading(90)  # Move up
            self.snake_screen.update()