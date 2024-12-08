from turtle import Turtle

# Create center line class:
class Center(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("silver")
        self.penup()
        self.goto(0, 0)
        self.shapesize(stretch_wid=0.5, stretch_len=26)
        self.setheading(90)
        
    