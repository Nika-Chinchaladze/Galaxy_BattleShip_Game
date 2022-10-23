from turtle import Turtle
from random import choice
COLORS = ["red", "crimson", "orange red", "deep pink", "gold"]


class RightBullets:
    def __init__(self):
        self.bullet_list = []

    def create_bullet(self, x_position, y_position):
        bullet = Turtle()
        bullet.penup()
        bullet.shape("square")
        bullet.shapesize(stretch_wid=0.25, stretch_len=0.75)
        bullet.color(choice(COLORS))
        bullet.setposition(x_position, y_position)
        bullet.setheading(180)
        self.bullet_list.append(bullet)

    def launch_bullet(self):
        for blt in self.bullet_list:
            blt.forward(20)

