from turtle import Turtle

class ScoreBoard(Turtle):
    """
    Contains everything related to the score board.
    """
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the score board.
        """
        self.goto(-150, 250)
        self.write(f"{self.left_score}", align="center", font=("Consolas", 30, "normal"))
        self.goto(150, 250)
        self.write(f"{self.right_score}", align="center", font=("Consolas", 30, "normal"))

    def left_point(self):
        """
        Add a point to the left side.
        """
        self.clear()
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        """
        Add a point to the left side.
        """
        self.clear()
        self.right_score += 1
        self.update_scoreboard()