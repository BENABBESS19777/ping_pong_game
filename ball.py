from turtle import Turtle

# Create paddle class:
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.shapesize(stretch_wid=1, stretch_len=1)
        