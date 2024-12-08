from turtle import Turtle

from turtle import Turtle

# Create paddle class:
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("gold")
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def up(self):
        """Move the paddle up by 20 units, if within screen bounds."""
        if self.ycor() < 250:  # Assuming the upper boundary is at y=250
            self.sety(self.ycor() + 20)

    def down(self):
        """Move the paddle down by 20 units, if within screen bounds."""
        if self.ycor() > -240:  # Assuming the lower boundary is at y=-240
            self.sety(self.ycor() - 20)
            