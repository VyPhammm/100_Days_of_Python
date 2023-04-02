# import colorgram as cg

# colors = cg.extract('Day18_Turtle-Graphics_Tuples\Hirst Painting\dot-image.jpg', 30)
# color_palette = []

# for color in colors :
#      r = color.rgb.r
#      g = color.rgb.g
#      b = color.rgb.b
#      new_color = (r, g, b)
#      color_palette.append(new_color)

# print(color_palette)

from turtle import Turtle, Screen, colormode, pos
import random

t = Turtle()
colormode(255)
# t.pensize(20)
t.speed(15)



color_list = [(202, 166, 109), (152, 73, 47), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]
t.hideturtle()

t.setheading(225)
t.penup()
t.forward(300)
t.setheading(0)
t.pendown()

def draw_one_row(n) :
     for _ in range(n) :
          t.dot(20, random.choice(color_list))
          t.penup()
          t.forward(50)

def upline() :
     t.setheading(90)
     t.forward(50)
     t.setheading(180)
     t.forward(500)
     t.setheading(0)

for _ in range(10) :
     draw_one_row(10)
     upline()








screen = Screen()
screen.exitonclick()
