# IMPORTS
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# SCREEN SETTINGS
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title(titlestring="Pong")
screen.tracer(0)  # Turn turtle animation on/off and set delay for update drawings

# ---------------------------------------------------------------------------------------------------------------
still_playing = True

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()



screen.listen()  # Set focus on TurtleScreen (in order to collect key-events)

screen.onkey(right_paddle.go_up, key="Up")  # .onkey: Bind fun to key-release event of key.
screen.onkey(right_paddle.go_down, key="Down")

screen.onkey(left_paddle.go_up, key="a")  # .onkey: Bind fun to key-release event of key.
screen.onkey(left_paddle.go_down, key="z")

while still_playing:
    time.sleep(ball.move_speed)  # sleep function is used to add delay in the execution of a program.
    screen.update()  # Perform a TurtleScreen update. To be used when tracer is turned off.
    ball.move()
    # DETECTING COLLISION WITH THE WALL
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    # DETECTING COLLISION WITH THE PADDLE
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.x_bounce()
    # DETECTING IF RIGHT PADDLE MISSES THE BALL
    if ball.xcor() > 380:
        scoreboard.left_point()
        scoreboard.update_scoreboard()
        ball.reset_pos()
    # DETECTING IF LEFT PADDLE MISSES THE BALL
    if ball.xcor() < -380:
        scoreboard.right_point()
        scoreboard.update_scoreboard()
        ball.reset_pos()
# ---------------------------------------------------------------------------------------------------------------
# SCREEN SETTINGS
screen.exitonclick()
