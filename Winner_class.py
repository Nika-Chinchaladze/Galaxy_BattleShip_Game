from turtle import Turtle


class Winner(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("wheat")
        self.setposition(0, 0)

    def declare_winner(self, winner):
        self.clear()
        self.write(f"GAME OVER, {winner} IS WINNER", align="center", font=("Courier", 22, "bold"))
