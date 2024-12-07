from turtle import Turtle

#Create paddle class:
def Paddle (Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
    
    def up(self):
        self.setheading(90)
        self.forward(20)
        
            