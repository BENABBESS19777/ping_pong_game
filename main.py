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
    ball.move(800, 600)
    #ball collision with paddles
    if ball.distance(left_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
        ball.speed("fastest")
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350:
        ball.bounce_x()
        ball.speed("fastest")
    #score handling
    if ball.xcor() > 390:
        scoreboard.increment_left_score()
        ball.reset_ball()
        ball.speed("normal")
    if ball.xcor() < -390:
        scoreboard.increment_right_score()
        ball.reset_ball()
        ball.speed("normal")
        
        
# ==================================================

screen.exitonclick()