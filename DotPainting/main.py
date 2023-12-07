import turtle
from turtle import Turtle, Screen
import random

#import colorgram

# colors = colorgram.extract('hirst.jpg', 30)
#
# rgb_colors = []
# for item in colors:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_set = [(230, 254, 241), (252, 236, 248), (253, 234, 85), (22, 1, 165), (195, 146, 137), (229, 225, 253),
             (123, 78, 248), (86, 252, 87), (248, 111, 166), (211, 107, 3), (4, 212, 210), (3, 139, 138), (44, 244, 51),
             (22, 123, 147), (149, 39, 244), (25, 4, 107), (9, 207, 213), (73, 1, 136), (138, 150, 210),
             (180, 172, 240), (228, 163, 210), (210, 117, 23), (122, 53, 180), (60, 6, 109), (131, 221, 226),
             (236, 165, 163), (7, 117, 113), (137, 20, 251)]

timmy = Turtle()
turtle.screensize(120, 120)
turtle.colormode(255)
timmy.penup()
timmy.hideturtle()
timmy.setpos(-200, -200)
timmy.speed("fastest")

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(color_set))
        timmy.forward(50)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.left(180)




screen = Screen()
screen.exitonclick()
