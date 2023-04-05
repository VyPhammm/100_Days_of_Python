from turtle import Turtle

STARTING_POSITION = [(0, 0), (0, 70), (0, 140),(0, 210), (0, 280), (0, -70), (0, -140),(0, -210), (0, -280)]

class CrossLine:

    def __init__(self) :
        for position in STARTING_POSITION :
            new_segment = Turtle("square")
            new_segment.shapesize(3, 0.1)
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)