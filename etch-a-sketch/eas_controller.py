class EasController:
    def __init__(self, turtle_class):
        self.turtle = turtle_class

    def up(self):
        self.turtle.setheading(90)
        self.check_boundary()
        self.turtle.forward(10)

    def down(self):
        self.turtle.setheading(270)
        self.check_boundary()
        self.turtle.forward(10)

    def left(self):
        self.turtle.setheading(180)
        self.check_boundary()
        self.turtle.forward(10)

    def right(self):
        self.turtle.setheading(0)
        self.check_boundary()
        self.turtle.forward(10)

    def check_boundary(self):
        x, y = self.turtle.xcor(), self.turtle.ycor()
        boundary_x = 720 // 2 - 10
        boundary_y = 720 // 2 - 10

        if x > boundary_x:
            self.turtle.setheading(180)  # Move left
        elif x < -boundary_x:
            self.turtle.setheading(0)  # Move right
        elif y > boundary_y:
            self.turtle.setheading(270)  # Move down
        elif y < -boundary_y:
            self.turtle.setheading(90)  # Move up