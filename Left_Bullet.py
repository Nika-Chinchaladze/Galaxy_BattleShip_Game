from turtle import Turtle
from random import choice
COLORS = ["pale green", "spring green", "green yellow", "lime", "lime green"]


class LeftBullets:
    def __init__(self):
        self.bullet_list = []

    def create_bullet(self, x_position, y_position):
        bullet = Turtle()
        bullet.penup()
        bullet.shape("circle")
        bullet.shapesize(0.5)
        bullet.color(choice(COLORS))
        bullet.setposition(x_position, y_position)
        bullet.setheading(0)
        self.bullet_list.append(bullet)

    def launch_bullet(self):
        for blt in self.bullet_list:
            blt.forward(20)
