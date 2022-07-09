import imp
from turtle import Turtle
import turtle

FONT = ("Fantasque Sans Mono", 16, "normal")
ALIGNMENT = "center"


class States(Turtle):
    def __init__(self, position, text):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(text, True, ALIGNMENT, FONT)
