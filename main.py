import colorgram
from turtle import *
import random as rd

jimmy = Turtle()
colors = colorgram.extract("hirst_spot_painting.jpg", 100)
color_tuple = []
colormode(255)
# print(screensize())
jimmy.penup()
jimmy.setpos(-300, -300)
jimmy.speed(0)
jimmy.hideturtle()
for i in colors:
    color_tuple.append((tuple(i.rgb)))
color_tuple.remove((246, 245, 243))
color_tuple.remove((233, 239, 246))
color_tuple.remove((246, 239, 242))
del color_tuple[0:2]
# print(color_tuple)
for i in range(1, 11):
    for j in range(1, 11):
        # jimmy.pendown()
        jimmy.dot(20, rd.choice(color_tuple))
        # jimmy.penup()
        jimmy.fd(50)
    jimmy.backward(50)
    jimmy.setheading(90)
    jimmy.fd(50)
    if (i + 1) % 2 == 0:
        jimmy.setheading(180)
    else:
        jimmy.setheading(0)
screen = Screen()
screen.exitonclick()
