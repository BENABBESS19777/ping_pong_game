from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from center import Center
from ball import Ball

# Create screen====================================
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
# ==================================================
# Create scoreboard object==========================
scoreboard = Scoreboard()
scoreboard.display_score()
# ==================================================
# Create paddle objects=============================
left_paddle= Paddle(-350, 0)
right_paddle = Paddle(350, 0)
# ==================================================
# Create center line
center_line = Center()
#===================================================
# Create ball object================================
ball = Ball()
#===================================================
# Control paddles with keyboard=====================
screen.listen()
screen.onkey(left_paddle.up, "w")  # Assuming Paddle class has an up method
screen.onkey(left_paddle.down, "s")  # Assuming Paddle class has a down method
screen.onkey(right_paddle.up, "Up")  # Assuming Paddle class has an up method
screen.onkey(right_paddle.down, "Down")  # Assuming Paddle class has a down method
# ==================================================
# Main game loop====================================
game_is_on = True
while game_is_on:
    screen.update()
    # Here you would typically add code to move the ball, check for collisions, etc.
# ==================================================

screen.exitonclick()