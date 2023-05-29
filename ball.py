from turtle import Turtle
from random import randint

MOVE_STEP = 20

class Ball(Turtle):
    """
    Contains everythin related to the ball.
    """
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """
        Makes the ball move.
        """
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)

    def y_bounce(self):
        """
        Changes direction of the ball bouncing related to axis y.
        """
        self.y_move *= -1

    def x_bounce(self):
        """
        Changes direction of the ball bouncing related to axis x(hitting a paddle).
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        """
        Sends ball to origin and changes direcction of movement.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()