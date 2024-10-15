from turtle import Turtle, Screen
from eas_controller import EasController

etcher = Turtle()
etcher_screen = Screen()
draw_controller = EasController(etcher)

# Display setup
etcher.shape("circle")
etcher.pensize(10)
etcher_screen.title("Etch a Sketch")
etcher_screen.setup(720, 720)

# Key press and release events
etcher_screen.onkeypress(draw_controller.up, "Up")
etcher_screen.onkeypress(draw_controller.down, "Down")
etcher_screen.onkeypress(draw_controller.left, "Left")
etcher_screen.onkeypress(draw_controller.right, "Right")

# Listen for events
etcher_screen.listen()

# Keep the program running
etcher_screen.mainloop()
