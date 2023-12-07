import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
race_on = False
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: \n(red, green, blue, "
                                             "yellow, orange, purple)")

colors = ["red", "green", "blue", "yellow", "orange", "purple"]

if user_bet not in colors:
    user_bet = screen.textinput("Make your bet", "Please chose one of the following colors to participate: \nred, "
                                                 "green, blue, yellow, orange, purple")

y_positions = [100, 60, 20, -20, -60, -100]

all_turtles = []

for racer in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[racer])
    new_turtle.penup()
    new_turtle.setpos(-230, y_positions[racer])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
