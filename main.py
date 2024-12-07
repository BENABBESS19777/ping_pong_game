from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle



#Create screen====================================
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
#=================================================

#Create scoreboard object=========================
scoreboard = Scoreboard()
scoreboard.display_score()
#=================================================

#Create paddle objects============================
left_paddle = Paddle((-290, 0))
right_paddle = Paddle((290, 0))
#==================================================








screen.exitonclick()