from turtle import Turtle


class LifeTracker:
    def __init__(self):
        self.writer = Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.color("white")
        # separate variables:
        self.left_life = 15
        self.right_life = 15

    def write_left_life(self):
        self.writer.clear()
        self.writer.setposition(-310, 180)
        self.writer.write(f"Life: {self.left_life}", align="left", font=("Courier", 18, "bold"))

    def write_right_life(self):
        self.writer.clear()
        self.writer.setposition(300, 180)
        self.writer.write(f"Life: {self.right_life}", align="right", font=("Courier", 18, "bold"))

    def draw_border(self):
        self.writer.setposition(0, 230)
        self.writer.setheading(270)
        self.writer.pendown()
        self.writer.forward(460)
        self.writer.penup()
