from turtle import Turtle

#Create a scoreboard==================================
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.display_score()
        
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))
        
                   
        