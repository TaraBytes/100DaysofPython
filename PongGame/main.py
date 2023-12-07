from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1 = Paddle(-350)
player_2 = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(player_2.up, "Up")
screen.onkeypress(player_2.down, "Down")
screen.onkeypress(player_1.up, "w")
screen.onkeypress(player_1.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.sleep_var)
    screen.update()
    ball.move()

#   # Detect collision with top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#   # Detect collision with right paddle
    if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.sleep_var *= 0.9

#   # Detect if ball goes out of bounds
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.left_point()
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.right_point()


screen.exitonclick()
