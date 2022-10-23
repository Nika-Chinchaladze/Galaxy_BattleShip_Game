from turtle import Turtle
Y_HIGH_CONTROL = 180
Y_LOW_CONTROL = -180
X_FRONT_CONTROL = 100
X_BACK_CONTROL = 300
MOVE_DISTANCE = 50


class RightWarShip(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("right_ship.gif")
        self.penup()
        self.setposition(300, 0)
        self.setheading(180)

    def move_up(self):
        x_place = self.xcor()
        y_place = self.ycor()
        if y_place < Y_HIGH_CONTROL:
            self.goto(x_place, y_place+MOVE_DISTANCE)

    def move_down(self):
        x_place = self.xcor()
        y_place = self.ycor()
        if y_place > Y_LOW_CONTROL:
            self.goto(x_place, y_place-MOVE_DISTANCE)

    def move_forward(self):
        if self.xcor() > X_FRONT_CONTROL:
            self.forward(MOVE_DISTANCE)

    def move_backward(self):
        if self.xcor() < X_BACK_CONTROL:
            self.backward(MOVE_DISTANCE)
