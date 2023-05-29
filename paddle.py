from turtle import Turtle

MOVE_STEP = 20

class Paddle(Turtle):
    """
    Contains everything related to the paddle.
    """
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    # MOVE FUNCTIONS
    def go_up(self):
        new_y = self.ycor() + MOVE_STEP
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_STEP
        self.goto(self.xcor(), new_y)


