from turtle import Turtle


ALIGNMENT = "center"
FONT = ("courier", 36, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.left_score, False, align=ALIGNMENT, font=FONT)
        self.goto(100, 240)
        self.write(self.right_score, False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()
