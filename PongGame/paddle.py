from turtle import Turtle
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 5)
        self.setheading(UP)
        self.penup()
        self.goto(x_position, 0)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)