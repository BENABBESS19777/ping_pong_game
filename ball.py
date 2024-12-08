from turtle import Turtle

# Create Ball class:
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.ball_dx = 1
        self.ball_dy = 1
        self.ball_speed = 1
        
    def reset_ball(self):
        self.goto(0, 0)
        self.ball_dx = 1  # Reset direction
        self.ball_dy = 1  # Reset direction
        
    def move(self, screen_width, screen_height):
        # Move the ball
        self.setx(self.xcor() + self.ball_dx * self.ball_speed)
        self.sety(self.ycor() + self.ball_dy * self.ball_speed)

        # Boundary checking
        if self.xcor() > screen_width / 2 or self.xcor() < -screen_width / 2:
            self.ball_dx *= -1  # Reverse direction on x-axis
        if self.ycor() > screen_height / 2 or self.ycor() < -screen_height / 2:
            self.ball_dy *= -1  # Reverse direction on y-axis

    def bounce_x(self):
        # Reverse the horizontal velocity to bounce off the paddle
        self.ball_dx *= -1  # Reverse direction on x-axis
           
        
        