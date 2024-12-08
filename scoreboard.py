from turtle import Turtle

# Create a scoreboard==================================
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.right_score_value = 0
        self.left_score_value = 0
        self.display_score()
    
    def increment_right_score(self):
        self.right_score_value += 1
        self.display_score()
    
    def increment_left_score(self):
        self.left_score_value += 1
        self.display_score()
            
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.left_score_value} : {self.right_score_value}", align="center", font=("Arial", 14, "normal"))